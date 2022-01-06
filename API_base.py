
from flask import Flask, request, Response

import traceback

import logging

import json



app = Flask(__name__)

@app.route('/base', methods=['POST'])
def receive_method():

    # Parametros de salida
    errorCode = 0
    errorMessage = ""
    response = ""
    resultCode = 0

    try:
        # parametros de entrada
        elasticParameters = request.json["elasticParameters"]


    except KeyError:
        errorCode = 1
        errorMessage = "JSON input malformed"
        resultCode = 1
        logging.info(traceback.format_exc())
        result = json.dumps({"errorCode": errorCode, "errorMessage": errorMessage, "response": response,
                             "resultCode": resultCode})
        resp = Response(result, status=200, mimetype="application/json")
        return resp

    else:
        result = json.dumps({"errorCode": errorCode, "errorMessage": errorMessage, "response": response,
                             "resultCode": resultCode})

        resp = Response(result, status=200, mimetype='application/json')
        return resp



###############################################

if __name__ == '__main__':
    app.run(host = 'localhost', port = 8057,debug=True)






