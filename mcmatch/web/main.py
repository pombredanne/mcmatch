'''
CherryPy application entry point

@author: niko
'''

import matplotlib
matplotlib.use('Agg')
    
import cherrypy, jinja2
from mcmatch.db.types import Codeblock, ObjectInfo
from mcmatch.feature.counter import counter_features
from mcmatch.feature import all_features, grouped_features
from mcmatch.feature.aggregator import FeatureAggregator
from mcmatch.analyze import KNearestNeighbors, DistanceInfo, TransformPipeline
from mcmatch.db.database import FunDB
from mcmatch.db.pg_database import PgFunDB
from mcmatch.web.form import CheckBox, Group, Form
from cherrypy._cperror import HTTPRedirect
from mcmatch.web.resulttree import FunctionTextTree
import StringIO
import os

env = jinja2.Environment(loader=jinja2.PackageLoader('mcmatch.web', 'webdata'))
code_sample_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "webdata/samples")

def mimetype(type):
  def decorate(func):
    def wrapper(*args, **kwargs):
      cherrypy.response.headers['Content-Type'] = type
      return func(*args, **kwargs)
    return wrapper
  return decorate


class Root(object):
  """CherryPy root application"""

  def _require_code(self):
    """returns the session loaded code, or throws a redirect error to the code load page."""
    if not 'code' in cherrypy.session:  # @UndefinedVariable
      raise HTTPRedirect('/update_code')
    return cherrypy.session['code']  # @UndefinedVariable

  def _optional_code(self):
    """Returns the loaded code or None."""
    if not 'code' in cherrypy.session: # @UndefinedVariable
      return None
    return cherrypy.session['code'] # @UndefinedVariable
  
  @cherrypy.expose
  def index(self):
    template = env.get_template('index.tpl.html')
    return template.render(title='index', code=self._optional_code())

  @cherrypy.expose
  def update_code(self):
    template = env.get_template('update_code.tpl.html')
    return template.render(title='set code to analyze',
                           samples=sorted(os.listdir(code_sample_path)))

  @cherrypy.expose
  def update_code_sample(self, sample):
    samples = os.listdir(code_sample_path)
    if not sample in samples:
      raise cherrypy.HTTPError(404, "Sample not found")
    f = open(os.path.join(code_sample_path, sample))
    cherrypy.session['code'] = f.read() # @UndefinedVariable
    f.close()
    raise HTTPRedirect("/")
    
  @cherrypy.expose
  def update_code_recv(self, code):
    cherrypy.session['code'] = code  # @UndefinedVariable
    raise HTTPRedirect('/')

  def _make_features(self, code):
    if code is None:
      return None
    if isinstance(code, Codeblock):
      cb = code
    else:
      cb = Codeblock()
      cb.disassembly_from_text(code)
    # TODO sort this somehow
    metr = FeatureAggregator(all_features.values())
    metr.calculate(cb)
    return metr.get_kv()
  
  @cherrypy.expose
  def fn_search(self, search=None, submit=None):
    functions = []
    fdb = PgFunDB()
    if search is not None:
      functions = list(fdb.get_functions_matching_signature(search, limit=300))

    template = env.get_template("find-fn.html")
    return template.render(title="Function search",
                           functions=functions,
                           search=search if search is not None else "")

  @cherrypy.expose
  def fn(self, id):
    fdb = PgFunDB()
    id = int(id)
    fun = fdb.get_function_by_id(id, include_disassembly=True)
    if not fun:
      raise cherrypy.HTTPError(404, "Function with ID %s not found" % id)

    c_mt = self._make_features(self._optional_code())
    f_mt = self._make_features(fun)

    template = env.get_template('fn.tpl.html')
    title = "showing function %d" % (fun.function_id)
    return  template.render(title=title, fun=fun, fmetr=f_mt, cmetr=c_mt, metr_keys=sorted(f_mt.keys()))

  @cherrypy.expose
  def repos(self, search=None, submit=None):
    if search is None:
      search = ""
    fdb = PgFunDB()
    repos_names = fdb.get_repository_names()
    repos_names = filter(lambda z: search in z, repos_names)
    template = env.get_template("repos.tpl.html")
    return template.render(title="repositories", repos=repos_names)

  @cherrypy.expose
  def repo(self, reponame):
    # TODO add support for reponame=None
    fdb = PgFunDB()
    object_ids  = fdb.get_objectids_matching(repository_is=reponame)
    objects = fdb.get_objects(object_ids)
    template = env.get_template("repo.tpl.html")
    return template.render(title="Repository %s" % (reponame), reponame=reponame, objects=objects)

  @cherrypy.expose
  def obj(self, id):
    fdb = PgFunDB()
    id = int(id)
    obj_ = fdb.get_object(id)
    if obj_ is None:
      raise cherrypy.HTTPError(404, "Object with ID %d not found" % id)
    
    assert isinstance(obj_, ObjectInfo)
    template = env.get_template('obj.tpl.html')
    title = 'showing object #%d' % (id)
    functions = list(fdb.get_functions_by_objectid(id))
    return template.render(title=title, obj=obj_,
        functions=functions)
  
  def _get_selected_ftids(self, flags):
    ftid_prefix = "ftid_"
    ftids = []
    for f in flags:
      #print f, flags[f]
      if f.startswith(ftid_prefix) and flags[f]:
        try:
          val = int(f[len(ftid_prefix):])
          ftids.append(val)
        except ValueError:
          pass
    return ftids
  
  def _make_ft_checkbox(self, ftid, flags):
    """create a checkbox selecting this function text id.
    
    We use function text ids instead of indices in the training
    data vector because, hopefully, a future version will allow us
    to manually select which repositories/objects constitute training
    data, and the indizes are thus subject to change."""
    
    checkbox_key = "ftid_%d" % ftid 
    checkbox = "<input type='checkbox' name='%s'" % checkbox_key
    if checkbox_key in flags and flags[checkbox_key]:
      checkbox += " checked='checked' "
    checkbox += "></input>"
    return checkbox
  
  def _get_index_from_ftid(self, ftids, function_text_ids):
    "maps function_text_ids.index(ftid) for each ftid in ftids"
    return [function_text_ids.index(ftid) for ftid in ftids]
  
  @cherrypy.expose
  def knn(self, submit=False, graph=False, **flags):
    code = self._require_code()
    
    # build options for features
    features = Group("features")
    for feature_group in grouped_features:
      for available_feature in sorted(grouped_features[feature_group].keys()):
        features.add(CheckBox(available_feature), feature_group)

    preprocessing = Group("preprocessing")
    preprocessing.add(CheckBox('ftrscale', 'feature scaling'))
    preprocessing.add(CheckBox('pca', 'PCA'))
    preprocessing.add(CheckBox('randompca', 'Random PCA'))
    preprocessing.add(CheckBox('kernelpca', 'Kernel PCA'))
    #preprocessing.add(CheckBox('lmnn', 'LMNN'))
    #preprocessing.add(CheckBox('nca', 'NCA'))
    
    form = Form()
    form.addGroup(features)
    form.addGroup(preprocessing)
    
    
    template = env.get_template('knn.tpl.html')
    if submit == False and graph == False:
      return template.render(title='K-NearestNeighbors', form_inner=form.getHTML(), result='')
    
    form.updateState(flags)
    
    selected_features = filter(lambda feature: form.g('features').k(feature).value, all_features)
    opt_feature_scaling = form.g('preprocessing').k('ftrscale').value * TransformPipeline.TRANSFORM_SCALE
    opt_pca = form.g('preprocessing').k('pca').value * TransformPipeline.TRANSFORM_PCA
    opt_random_pca = form.g('preprocessing').k('randompca').value * TransformPipeline.TRANSFORM_RANDOM_PCA
    opt_kernel_pca = form.g('preprocessing').k('kernelpca').value * TransformPipeline.TRANSFORM_KERNEL_PCA
    #opt_lmnn = form.g('preprocessing').k('lmnn').value * TransformPipeline.TRANSFORM_LMNN
    #opt_nca = form.g('preprocessing').k('nca').value * TransformPipeline.TRANSFORM_NCA
    
    transform = opt_feature_scaling + opt_pca + opt_random_pca + opt_kernel_pca # + opt_lmnn + opt_nca
    
    
    c = Codeblock()
    c.disassembly_from_text(code)
    print c.get_mnemonic_histogram()
    metr = FeatureAggregator([all_features[m] for m in selected_features])
    fdb = PgFunDB()
    repos = list(fdb.get_repository_names())
    # TODO add select mode
    #repos = [r if r is not "None" else None for r in repos]
    repos = filter(lambda n: n != "musl-1.1.6" and n != 't-glibc', repos)
    knn = KNearestNeighbors(fdb, metr, 100, opt_feature_scaling, training_repositories=repos)
    distances, ft_info = knn.get_neighbours(c)

    function_text_ids = [f[0] for f in ft_info]
    # cache compileroptions for all loaded functions
    fdb.precache_containing_objects(fn_textids=function_text_ids)

    result = []
    valueRange = (1e20, 0)
    for i in range(0, len(distances[0])):
      valueRange = (min(valueRange[0], distances[0][i]), max(valueRange[1], distances[0][i]))
      result.append((self._make_ft_checkbox(function_text_ids[i], flags), ("%6f" % distances[0][i]), FunctionTextTree(fdb, function_text_ids[i])))
    
    plotsrc = None
    if graph:
      nn = DistanceInfo(fdb, metr, opt_feature_scaling, None, "euclidean")
      dists, tb_info = nn.test_codeblock(c)
      function_text_ids_ = [f[0] for f in nn.get_trainingset_infos()]
      additional_ftdids = []
      if 'add_ftdids' in flags:
        additional_ftdids = [int(z) for z in flags['add_ftdids'].split(",")]
      equivalences = self._get_index_from_ftid(self._get_selected_ftids(flags) + additional_ftdids,
                                               function_text_ids_)
      function_names = [nn.get_trainingset_infos()[idx][1] for idx in equivalences]
      tb_info = (-1, "md5_process_block")
      nn.make_graph_single(dists[0], tb_info, equivalences,
                           valueRange=(valueRange[0]*0.9, valueRange[1]*1.8),
                           equiNames=function_names)
      plotsrc = self._pyplot_to_inline_image()
        
    return template.render(title='K-NearestNeighbors',
                           form_inner=form.getHTML(),
                           result=result,
                           plotsrc=plotsrc)

  def _pyplot_to_inline_image(self):
    import matplotlib.pyplot as plt
    import base64
    imgdata = StringIO.StringIO()
    plt.savefig(imgdata, format="png")
    imgdata.seek(0)
    imgdata = imgdata.read()
    imgdata = base64.b64encode(imgdata)

    plt.savefig("_last-graph.pdf")
    plt.close()
    return "data:image/png;base64," + imgdata
      
  @cherrypy.expose
  @mimetype("text/javascript")
  def js(self):
    return """
function toggle_visibility(id) { el = document.getElementById(id);
if (el.style.display == 'none') { el.style.display='block'; } else { el.style.display='none'; }};"""
