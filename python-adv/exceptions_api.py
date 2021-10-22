from os import error
from flask import Flask, request
from flask.wrappers import Response
# import logging
# from flask_gcp_log_groups import GCPHandler

app = Flask(__name__)

# g = GCPHandler(app, parentLogName="request",
#     childLogName="application",
#     traceHeaderName='X-Cloud-Trace-Context',
#     labels= {'foo': 'bar', 'baz': 'qux'},
#     resource= {
#                 "type": "gce_instance", 
#                 "labels": { "instance_id": "5160310737730769780",
#                             "zone": "us-central1-a" 
#                           }
#     }
#   )
# g.setLevel(logging.INFO)
# app.logger.addHandler(g)

@app.route('/', methods=['GET'])
def root():
    return "v0.1"

@app.route('/healthz', methods=['GET'])
def healthz():
    return "ok"

@app.route('/star', methods=['GET'])
def hello_world():
    num = request.args.get('num', '')
    
    try:
        x = 1 / int(num)

        return str(x) 

    except:
        return "does not work", 400

@app.route('/nws')
def nws():
    num = request.args.get('num', '')

    try:
        x = 1 / int(num)

        return str(x) 

    except:
        return "does not work", 500

if __name__ == '__main__':
    app.run(debug=False, port=6000,host='0.0.0.0')