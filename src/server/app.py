# run using `nodemon --exec "python" src/server/app.py` to detect filechanges

# TODO: separate this into modules, e.g. utils.py / config.py / serve.py
import logging
import pickle
from sys import exit
from os import environ
from jsonrpc import JSONRPCResponseManager, dispatcher # if this crashes, run `pip install jsonrpc`
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
from werkzeug.debug import DebuggedApplication

def load():
  try:
    with open(data_path, 'rb') as fin:
      return pickle.load(fin)
  except:
    print 'data store not created. initializing to {}'
    return {}

def save(data):
  with open(data_path, 'wb') as fout:
    pickle.dump(data, fout)

if __name__ == '__main__':
  env_version = '1'
  if 'ENV_VERSION' not in environ or environ['ENV_VERSION'] != env_version:
    print 'Run `. env.sh` from the root project directory'
    exit(0)

  root = environ['MOO_ROOT']
  port = environ['MOO_PORT']
  data_path = '%s/data/data.p' % root

  logging.basicConfig()

  @dispatcher.add_method
  def testRPC(a, b):
    return {'the sum is': a + b}

  @Request.application
  def application(request):
    response = JSONRPCResponseManager.handle( request.data, dispatcher)
    return Response(response.json, mimetype='application/json')

  print 'serving on port', port
  run_simple('localhost', port, application)
