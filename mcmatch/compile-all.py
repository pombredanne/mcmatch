import sys, os
from subprocess import call

def die(error):
    print "Error:", error
    sys.exit(1)

def build(fname):
    if not fname.endswith(".c"):
        die("called with invalid fname %s" % fname)
    fbase = fname[:-2]
    fout = fbase + ".o"
    print "building", fname
    cmd = "gcc -std=c99 -w -I. -O2 -c -g -o %s %s" % (fout, fname)
    os.system(cmd)

def build_all(path):
    for f in os.listdir(path):
        if f.endswith(".c"):
            build(f)

build_all(".")
