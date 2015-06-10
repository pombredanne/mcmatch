'''
PostgreSQL database backend

@author: niko
'''
import psycopg2, os
from database import FunDB
from types import Fn, ObjectInfo
from mcmatch.db.types import FnFeature
import numpy as np
import logging
from mcmatch.feature.aggregator import FeatureAggregator
import hashlib
from mcmatch.db.compileroptions import CompilerOptions

PG_DSN="dbname=niko"

logger = logging.getLogger(__name__)

class PgFunDB(FunDB):
  conn = None
  
  object_cache = {}
  last_instance = None

  def __init__(self, dsn=None, conn=None):
    if dsn is None:
      dsn = PG_DSN
    
    if conn is None:
      conn = psycopg2.connect(dsn)
    
    assert isinstance(conn, psycopg2._psycopg.connection)
    self.conn = conn
    
    PgFunDB.last_instance = self
  
  def update_function_count(self):
    cursor = self.conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM functions;")
    self.function_count = cursor.fetchone()[0]
  
  def save(self):
    self.conn.commit()
  
  def load(self):
    self.update_function_count()
  
  def needs_update(self, object_file_name):
    objpath = os.path.abspath(object_file_name)
    curmodts = os.stat(objpath).st_mtime
    
    cursor = self.conn.cursor()
    cursor.execute("SELECT extract(epoch from mtime) FROM objects WHERE filepath = %s;",
                   (objpath,))
    row = cursor.fetchone()
    if row is None:
      return True
    
    storedmodts = row[0]
    
    # Somewhere in the DB conversion, the mtime timestamp looses
    # presision.
    t_eps = 0.05
    
    print curmodts, storedmodts, curmodts-storedmodts
    print curmodts-t_eps > storedmodts
    if (curmodts-t_eps) > storedmodts:
      return True
    return False


  def store_object(self, objectinfo):
    """stores the given ObjectInfo object, 
    along with all contained functions and the
    CompilerOptions"""
    
    assert isinstance(objectinfo, ObjectInfo)
    objpath = os.path.abspath(objectinfo.get_path())
    mtime = objectinfo.get_mtime()
    
    self.delete_objects_by_filename(objpath, delete_locked_files=False)
    
    cursor = self.conn.cursor()
    
    cursor.execute("""
      INSERT INTO objects 
        ( filepath, mtime, """ 
        + CompilerOptions.get_sql_field_names()
        + """ )
      VALUES (%s, to_timestamp(%s), """
        + ",".join(["%s"]*CompilerOptions.get_sql_field_count())
        + """ )
      RETURNING id;""", (objpath, mtime) + tuple(objectinfo.get_compileopts().get_sql_field_data()))
    row = cursor.fetchone()
    object_id = int(row[0])
    
    for fun in objectinfo.get_functions_by_shortname():
      assert isinstance(fun, Fn)
      disassembly_text = fun.disassembly_to_text()
      text_hash = hashlib.sha1(fun.sig + "\0" + disassembly_text).digest()
      text_hash = psycopg2.Binary(text_hash)
      cursor.execute("""
        SELECT id FROM function_text WHERE hash = %s
      """, (text_hash,))
      row = cursor.fetchone()
      if not row:
        cursor.execute("""
          INSERT INTO function_text
            (hash, signature, disassembly)
          VALUES
            (%s, %s, %s)
          RETURNING id""",
          (text_hash, fun.sig, disassembly_text))
        row = cursor.fetchone()
      text_id = row[0]
      cursor.execute("""
      INSERT INTO functions
        (objectID, name, signature, source_file, function_text_id)
      VALUES
        (%s, %s, %s, %s, %s);
      """, (object_id, fun.name, fun.sig, fun.source_file, text_id))
    
    return object_id


  def _yield_fnquery_rows(self, cursor, includes_disassembly):
    """loop over all rows from the cursor, yield Fn
    objects"""
    row = cursor.fetchone()
    #print "row is", row
    while row:
      fn = Fn.from_sql_row(row, includes_disassembly)
      yield fn
      row = cursor.fetchone()


  def all_functions(self, include_disassembly=False):
    cursor = self.conn.cursor()
    cursor.execute(Fn.get_sql_select(include_disassembly))
    for i in self._yield_fnquery_rows(cursor, include_disassembly):
      yield i


  def get_functions_by_shortname(self, functions, debug=True):
    return self._get_functions_slow(functions, debug)


  def get_function_by_id(self, fid, include_disassembly=False):
    """
    rtype: Fn
    Return function by id or None"""
    # TODO allow this function to also fetch the associated
    # object.
    cursor = self.conn.cursor()
    cursor.execute(Fn.get_sql_select(include_disassembly) + " WHERE functions.id = %s""", (fid,))
    row = cursor.fetchone()
    if not row:
      return None

    return Fn.from_sql_row(row, include_disassembly)


  def get_functions_matching_signature(self, signature, limit=300, include_disassembly=False):
    cursor = self.conn.cursor()
    limits = ""
    if limit is not None:
      limits = " LIMIT %d" % limit

    cursor.execute(Fn.get_sql_select(include_disassembly) + " WHERE signature ILIKE '%%'||%s||'%%'" + limits, (signature,))

    for i in self._yield_fnquery_rows(cursor, include_disassembly):
      yield i


  def get_functions_with_textid(self, textid, include_disassembly=False):
    cursor = self.conn.cursor()
    cursor.execute(Fn.get_sql_select(include_disassembly) + " WHERE function_text_id = %s", (textid,))
    
    for i in self._yield_fnquery_rows(cursor, include_disassembly):
      yield i


  def get_functions_by_objectid(self, objectid, include_disassembly=False):
    cursor = self.conn.cursor()
    cursor.execute(Fn.get_sql_select(include_disassembly) + " WHERE objectid = %s", (objectid,))
    for i in self._yield_fnquery_rows(cursor, include_disassembly):
      yield i

  def get_functions_by_repository(self, reponame, include_disassembly=False):
    cursor = self.conn.cursor()
    cursor.execute(Fn.get_sql_select(include_disassembly) + " JOIN objects ON functions.objectid = objects.id WHERE objects.repository = %s",
        (reponame,))
    for i in self._yield_fnquery_rows(cursor, include_disassembly):
      yield i

  def get_function_texts_by_repository(self, reponames, include_disassembly=False):
    """return a tuple (textid, signature, disassembly). The last element is optional
    and is only returned with include_disassembly=True.
    """
    if not isinstance(reponames, list):
      if not isinstance(reponames, str):
        raise Exception("reponames is neither string nor list")
      reponames = [reponames]

    cursor = self.conn.cursor()
    statement = """SELECT
                   DISTINCT(function_text.id), function_text.signature"""
    if include_disassembly:
      statement += ", function_text.disassembly "

    statement += """
                    FROM function_text
                    JOIN functions
                      ON functions.function_text_id = function_text.id
                    JOIN objects
                      ON objects.id = functions.objectid
                    WHERE objects.repository = ANY(%s)"""
    logger.debug("executing " + statement)
    cursor.execute(statement, (reponames,))
    for row in cursor:
      yield tuple(row)


  def delete_objects_by_filename(self, filename, delete_locked_files=False):
    objpath = os.path.abspath(filename)
    cursor = self.conn.cursor()
    if delete_locked_files:
      cursor.execute("DELETE FROM objects WHERE filepath = %s",
                     (objpath,))
    else:
      cursor.execute("DELETE FROM objects WHERE filepath = %s AND locked = 'f'",
                     (objpath,))


  def delete_object(self, object_id, delete_locked_file=True):
    cursor = self.conn.cursor()
    if delete_locked_file:
      cursor.execute("DELETE FROM objects WHERE id = %s", (object_id,))
    else:
      cursor.execute("DELETE FROM objects WHERE id = %s WHERE locked = 'f'", (object_id,))


  def lock_object(self, object_id, locked=True):
    """Set "locked" flag on the given object"""
    cursor = self.conn.cursor()
    cursor.execute("UPDATE objects SET locked = %s WHERE id = %s",
                   (locked, object_id,))


  def lock_objects_by_path(self, path, locked=True, exact_match_only=True):
    """Set 'locked' flag on objects matching the given path.
    If exact_match_only is set to false, all subpaths (path*) will be
    matched."""
    cursor = self.conn.cursor()
    if exact_match_only:
      cursor.execute("UPDATE objects SET locked = %s WHERE filepath = %s",
                     (locked, path,))
    else:
      cursor.execute("UPDATE objects SET locked = %s WHERE filepath LIKE %s",
                     (locked, path + "%",))


  def get_objectids_by_filename(self, filepath, mtime=None, first_only=True):
    """returns object IDs for a given filepath. If mtime is not None,
    the mtime has to match within eps=+/-0.01.
    
    If first_only is True, returns the first matching object_id
    or None if there is no such object.
    If first_only is False, returns a list of all matching object_ids
    (or an empty list)""" 
    cursor = self.conn.cursor()
    if mtime is None:
      cursor.execute("SELECT id FROM objects WHERE filepath = %s",
                   (filepath))
    else:
      cursor.execute("SELECT id FROM objects WHERE filepath = %s AND mtime >= to_timestamp(%s) AND mtime <= to_timestamp(%s)",
                   (filepath, mtime-0.01, mtime+0.01))
    
    rows = cursor.fetchall()
    rows = [int(x[0]) for x in rows]
    if first_only:
      if len(rows):
        return rows[0]
      return None
    return rows

  class FunctionTextQueryOptions:
    def __init__(self, with_id=None, with_missing_features=None, include_disassembly=True):
      """Query filter for function texts.
      - with_id: int or [int]. Only tuples with these function_text_ids will be returned.
      - include_disassembly: Wether to include the full function text in the return value.
      - with_missing_features: A list with FnFeature types. Return value will only include
                              function texts where at least one feature is missing in the
                              database.
      """
      self.with_id = with_id
      if self.with_id is not None:
        if isinstance(self.with_id, int) or isinstance(self.with_id, long):
          self.with_id = [self.with_id]
  
        if not isinstance(self.with_id, list):
          raise Exception("Unexpected argument in 'id' field: %r" % (with_id,))

      self.with_missing_features = with_missing_features
      self.include_disassembly = include_disassembly
      self.input_tuple = []

      self._prepare_where()

    def _prepare_where(self):
      """Return the "WHERE" part of the query, including the "WHERE"."""
      where = []
      if self.with_missing_features:
        missing_feature_where = []
        for feature in self.with_missing_features:
          assert isinstance(feature, FnFeature)
          missing_feature_where.append("id NOT IN (SELECT function_text_id FROM " + feature.get_sql_table() + ")\n")
        where.append(" OR ".join(missing_feature_where))

      if self.with_id:
        where.append("function_text.id = ANY(%s)")
        self.input_tuple.append(self.with_id)

      if not len(where):
        self._where = ""
      else:
        self._where = " WHERE " + " AND ".join(where)

    def field_list(self):
      fl = " function_text.id, function_text.signature "
      if self.include_disassembly:
        fl += " , function_text.disassembly "
      return fl

    def where(self):
      return self._where

    def data(self, as_list=False):
      """return the tuple required for the input. Note that input will be generated in order of
      calling of the statement generating functions."""
      if as_list:
        return self.input_tuple
      return tuple(self.input_tuple)

    def full_statement(self):
      """helper function, returns the full SELECT statement"""
      return """SELECT %s FROM function_text %s""" % (self.field_list(), self.where())

  def get_function_texts(self, with_id=None, with_missing_features=None, include_disassembly=True):
    """returns a tuple (text_id, function signature, disassembly)"""
    query = self.FunctionTextQueryOptions(with_id=with_id, with_missing_features=with_missing_features, include_disassembly=include_disassembly)
    cursor = self.conn.cursor()
    cursor.execute(query.full_statement(), query.data())
    return cursor.fetchall()

  def get_objectids_matching(self,
                             has_features=None,
                             path_contains=None,
                             filename_contains=None,
                             filename_is=None,
                             repository_is=None,
                             path_is=None):
    where = []
    sql_input = []
    #if has_features is not None:
    #  where.append(" has_features = %s ")
    #  sql_input.append(has_features)
    if path_contains is not None:
      where.append(" filepath ILIKE %s ")
      sql_input.append("%" + path_contains + "%")
    if path_is is not None:
      where.append(" filepath = %s ")
      sql_input.append(path_is)
    if filename_contains is not None:
      where.append(" regexp_replace(filepath, '.+/', '') ILIKE %s ")
      sql_input.append("%" + filename_contains + "%")
    if filename_is is not None:
      where.append(" regexp_replace(filepath, '.+/', '') = %s ")
      sql_input.append(filename_is)
    if repository_is is not None:
      where.append(" repository = %s ")
      sql_input.append(repository_is)
    if len(where):
      where = "WHERE " + (" AND ".join(where))
    else:
      where = ""
    sql_input = tuple(sql_input)
    cursor = self.conn.cursor()
    logger.debug("SQL: %s %r" % (where, sql_input))
    cursor.execute("SELECT id FROM objects " + where, sql_input)
    row = cursor.fetchone()
    ids = []
    while row:
      ids.append(row[0])
      row = cursor.fetchone()
    return ids
  
  def set_compiler_options(self, obj):
    assert isinstance(obj, ObjectInfo)
    cursor = self.conn.cursor()
    co = obj.get_compileopts()
    assert isinstance(co, CompilerOptions)
    obj_id = obj.id
    if obj.locked:
      raise RuntimeError("set_compiler_options(objid=%d) attempted to modify locked object"
                         % obj.id)
    cursor.execute("""UPDATE objects
    SET """ + co.get_sql_field_names(as_update_s=True) + """
    WHERE id = %s
    """, tuple(co.get_sql_field_data()) + (obj_id,))


  def set_compiler_options_by_path(self, objpath, expected_mtime, compileroptions):
    assert isinstance(compileroptions, CompilerOptions)

    objids = self.get_objectids_matching(path_contains=objpath)
    if not len(objids):
      return False
    objs = self.get_objects(objids)
    
    num_updates = 0
    total = 0
    mtime_failures = 0
    locked_objects = 0
    for obj in objs:
      total += 1
      if obj.locked:
        locked_objects += 1
        continue
      if abs(obj.mtime - expected_mtime) < 0.1:
        num_updates += 1
        obj.set_compileopts(compileroptions)
        self.set_compiler_options(obj)
      else:
        mtime_failures += 1
    
    logger.info("updated %d of %d objects matching path %s" %
                 (num_updates, total, objpath))
    if mtime_failures > 0:
      logger.warning("%d objects not updated because mtime did not match" % mtime_failures)
    if locked_objects > 0:
      logger.warning("%d objects not updated because they have been locked in database." % locked_objects)
    if not num_updates:
      return None
    
    return num_updates


  def _get_objects(self, objectids=None):
    'rtype: ObjectInfo'
    cursor = self.conn.cursor()
    where_clause = ""
    input_tuple = tuple()
    if objectids is not None:
      where_clause = "WHERE id = ANY (%s)"
      input_tuple = (list(objectids),)
      
    cursor.execute("""SELECT 
    filepath, extract(epoch from mtime), locked,
    """ + CompilerOptions.get_sql_field_names() + """, id
    FROM objects """ + where_clause,
      input_tuple)
    
    objs = []
    row = cursor.fetchone()
    while True:
      if not row:
        return objs
      filepath = row[0]
      mtime = row[1]
      locked = row[2]
      row = row[3:]
      opt = CompilerOptions.from_sql_row(row)
      row = row[CompilerOptions.get_sql_field_count():]
      objectid = row[0]
      
      obj = ObjectInfo(filepath, mtime, None, False, objectid)
      obj.locked = locked
      obj.set_compileopts(opt)
      PgFunDB.object_cache[objectid] = obj
      objs.append(obj)
      row = cursor.fetchone()
    return objs

  def get_object(self, objectid):
    'rtype: ObjectInfo'
    if objectid in PgFunDB.object_cache:
      return PgFunDB.object_cache[objectid]
    objs = self._get_objects([objectid])
    if not len(objs):
      return None
    return objs[0]
  
  def get_objects(self, objectids):
    # TODO check whether some of these exist already?
    return self._get_objects(objectids)
      
  def precache_containing_objects(self, fns=None, fn_textids=None):
    """
    accepts a list of Fn objects or function text ids.
    return a dictionary mapping from objectid to object path.
    
    If the list of functions is None, all objects will be
    cached."""
    if fns is None and fn_textids is None:
      return self._get_objects(None)
    
    objectids = set()
    if fns is None and fn_textids is not None:
      cursor = self.conn.cursor()
      # TODO this could be turned into a single JOIN within the _get_objects call
      cursor.execute("""SELECT objectid
                        FROM functions
                        WHERE function_text_id = ANY (%s)""", (fn_textids,))
      for row in cursor:
        objectids.add(row[0])
    elif fns is not None and fn_textids is None:
      for fn in fns: #: :type fn: Fn
        objectids.add(fn.get_container_object_id())
    else:
      raise Exception("Invalid parameters to get_objects()")
    return self._get_objects(objectids)
    
  def get_compiler_options(self, objectid):
    'rtype: CompilerOptions'
    obj = self.get_object(objectid)
    if not obj:
      return None
    return obj.get_compileopts()
  
  def store_features(self, function_text_id, features):
    cursor = self.conn.cursor()
    assert isinstance(function_text_id, int)
    assert isinstance(features, FnFeature)
    
    mntable = features.get_sql_table()
    
    cursor.execute("DELETE FROM " + mntable + " WHERE function_text_id = %s",
                   (function_text_id,))
    
    column_list = ("(function_text_id, " +
      ",".join(features.get_sql_columns(fq_select=False)) + ")")
    sql_values = features.get_sql_contents()
    value_list = "(%s, " + ",".join(["%s"]*len(sql_values)) + ")"
    value_tuple = tuple([function_text_id] + sql_values)

    cursor.execute("INSERT INTO " + mntable + " "
                   + column_list + " VALUES " +
                   value_list,
                   value_tuple)


  def get_features_np(self, fnfeature, in_repositories=None, include_signature=True):
    """returns a tuple (function_text_info, associated_features as numpy array).
    function_text_info is a list with each entry corresponding to each row in associated_features.
    if include_signature is set to True, each entry in the list will be a tuple (function_text_id, function_signature),
      otherwise it will only be an integer.
    if in_repositories is not None, it should be either a string or a list of strings, describing (OR-connected) the
    repositories that should be selected.
    """
    # TODO this will cause problems on larger datasets.
    assert isinstance(fnfeature, FnFeature)
    if in_repositories is not None:
      if isinstance(in_repositories, str):
        in_repositories = [in_repositories]
      if ((not isinstance(in_repositories, list))
          or (len(in_repositories) == 0)
          or (not isinstance(in_repositories[0], str))):
        raise ValueError("in_repositories must be either str or list[str], list must not be empty")

    cursor = self.conn.cursor()

    sqltable = None
    has_view = False
    if isinstance(fnfeature, FeatureAggregator):
      has_view = True
      sqltable = 'aggregated_cluster_view'
      select, inp, data_offset = fnfeature.get_sql_select(in_repositories=in_repositories, include_signature=include_signature)
      statement = ("CREATE TEMPORARY VIEW " + sqltable +" AS " + select)
      logger.debug(statement)
      cursor.execute(statement, (inp,))
    else:
      raise NotImplemented("this code path is currently unavailable")
      sqltable, _ = fnfeature.get_sql_table()

    cursor.execute("SELECT COUNT(*) FROM " + sqltable)
    row = cursor.fetchone()
    num_rows = int(row[0])
    num_cols = len(fnfeature.get_sql_columns())

    ids = []
    data = np.empty((num_rows, num_cols))

    cursor.execute("SELECT * FROM " + sqltable)

    row = cursor.fetchone()
    i = 0
    while row:
      ids.append(row[0:data_offset])
      data[i] = row[data_offset:]
      i += 1
      row = cursor.fetchone()

    if has_view:
      cursor.execute("DROP VIEW " + sqltable)
    return (ids, data)

  def recreate_features_table(self, fnfeature):
    # TODO allow class type as well (not just instance)
    assert isinstance(fnfeature, FnFeature)

    cursor = self.conn.cursor()
    table_name = fnfeature.get_sql_table()

    cursor.execute("DROP TABLE IF EXISTS " + table_name)

    cts = ("CREATE TABLE " + table_name + " (" + fnfeature.create_table_ddl()
                   + ") INHERITS(features)")
    logging.info(cts)
    cursor.execute(cts)

  def delete_feature_data(self, fnfeature):
    assert isinstance(fnfeature, FnFeature)

    cursor = self.conn.cursor()
    table_name = fnfeature.get_sql_table()

    cursor.execute("DELETE FROM " + table_name)

  def delete_stale_features(self):
    cursor = self.conn.cursor()
    cursor.execute("DELETE FROM features WHERE function_text_id NOT IN (SELECT id FROM function_text)")

  def get_repository_names(self):
    cursor = self.conn.cursor()
    cursor.execute("SELECT DISTINCT(repository) FROM objects")
    for row in cursor:
      if row[0] is None or row[0] == "":
        yield "None"
      else:
        yield row[0]
  
  def get_function_count(self):
    """Returns the amount of registered functions"""
    cursor = self.conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM functions")
    return cursor.fetchone()[0]

  def delete_stale_functiontexts(self):
    cursor = self.conn.cursor()
    cursor.execute("DELETE FROM function_text WHERE id NOT IN (SELECT function_text_id FROM functions)")
    self.save()
    return
