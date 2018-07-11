#!/usr/bin/python
activate_this = '/opt/app-root/lib64/python3.6/os.py'
#execfile(activate_this, dict(__file__=activate_this))
import os

virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
#virtenv = os.path.join(os.environ.get('OPENSHIFT_PYTHON_DIR','.'), 'virtenv')
virtualenv = os.path.join(virtenv, 'activate_this')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass
#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

from flaskapp import app as application

#
# Below for testing only
#

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    ip = os.environ['OPENSHIFT_PYTHON_IP']
    port = int(os.environ['OPENSHIFT_PYTHON_PORT'])
    #host_name = os.environ['OPENSHIFT_GEAR_DNS']
    httpd = make_server(ip, 8080, application)
    #httpd = make_server('localhost', 8051, application)
    # Wait for a single request, serve it and quit.
    httpd.handle_request()
    #httpd.serve_forever()
