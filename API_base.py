
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
    status = 200
    result = json.dumps({"errorCode": errorCode, "errorMessage": errorMessage, "response": response,
                         "resultCode": resultCode})

    try:
        # Parametros de entrada
        params = request.json["params"]


    except KeyError:
        errorCode = 1
        errorMessage = "JSON input malformed"
        resultCode = 1
        status = 404
        result = json.dumps({"errorCode": errorCode, "errorMessage": errorMessage, "response": response,
                             "resultCode": resultCode})
        logging.error(traceback.format_exc())


    else:
        # Todo bien
        pass

        result = json.dumps({"errorCode": errorCode, "errorMessage": errorMessage, "response": response,
                             "resultCode": resultCode})
        resp = Response(result, status=status, mimetype='application/json')
        return resp
    finally:
        # Ocurrio algun error
        pass

        resp = Response(result, status=status, mimetype="application/json")
        return resp



###############################################

if __name__ == '__main__':
    app.run(host = 'localhost', port = 8057,debug=True)






