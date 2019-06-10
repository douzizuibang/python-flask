import sys
sys.path.append("..")
import flask
from model.model import model

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def entry():
    return flask.Response('System is running...')

@app.route('/hello/', methods=['GET'])
def put_disaster_score(user_id, project_id):
    print "hello world for openshift"
    return flask.Response('hello world for openshift for flask in python')

if __name__ == '__main__':
    PORT = 5000
    app.run(host='0.0.0.0', port=PORT)
