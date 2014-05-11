import os

virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass
#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from hello import app

http_server = HTTPServer(WSGIContainer(app))
ip   = os.environ['OPENSHIFT_PYTHON_IP']
port = int(os.environ['OPENSHIFT_PYTHON_PORT'])

http_server.listen(port, ip)
IOLoop.instance().start()

# from gevent.wsgi import WSGIServer
# from hello import app

# ip   = os.environ['OPENSHIFT_PYTHON_IP']
# port = int(os.environ['OPENSHIFT_PYTHON_PORT'])

# http_server = WSGIServer((ip, port), app)
# http_server.serve_forever()