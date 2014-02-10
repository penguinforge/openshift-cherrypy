#!/usr/bin/env python
import imp
import os

#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

#
#  main():
#

if __name__ == '__main__':
   ip   = os.environ['OPENSHIFT_PYTHON_IP']
   port = int(os.environ['OPENSHIFT_PYTHON_PORT'])
   app = imp.load_source('application', 'wsgi/application')

   fwtype="wsgiref"
   for fw in ("cherrypy"):
      try:
         imp.find_module(fw)
         fwtype = fw
      except ImportError:
         pass

   print('Starting WSGIServer type %s on %s:%d ... ' % (fwtype, ip, port))
   if fwtype == "cherrypy":
      from cherrypy import wsgiserver
      server = wsgiserver.CherryPyWSGIServer(
         (ip, port), app.application, server_name=os.environ['OPENSHIFT_APP_DNS'])
      server.start()

   else:
      from wsgiref.simple_server import make_server
      make_server(ip, port, app.application).serve_forever()
