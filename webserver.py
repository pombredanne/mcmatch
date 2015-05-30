#!/usr/bin/python2
'''
Created on Jan 5, 2015

@author: niko
'''
from sklearn.neighbors import NearestNeighbors, KDTree

import cherrypy
from mcmatch.db.types import FnDiff
from mcmatch.web.main import Root
import argparse

def main():
  parser = argparse.ArgumentParser(description="run the built-in webserver")
  parser.add_argument('-p', '--port', type=int, help="port to run on", default=8080)
  args = parser.parse_args()

  cherrypy.config.update({'server.socket_port': args.port})


  conf =  {
          '/':  {
                'tools.sessions.on': True,
                'tools.sessions.storage_type': "file",
                'tools.sessions.storage_path': "/tmp/"
                }
          }
  cherrypy.quickstart(Root(), '/', conf)


if __name__ == '__main__':
  main()

