from flask import jsonify, make_response, request, Flask
import base64
from datetime import datetime
import itertools

app = Flask(__name__)

id = itertools.count()
URLS = []

@app.route('/urlinfo/<int:version>/<url>', methods=["GET"])
def get_url(version, url):
    """Function to retreive a URL from the API"""

    if version == 1 and url and request.method == "GET":

        if isBase64(url):
            try:
                #Get URL here
                url_info = next((item for item in URLS if item["base64_url"] == f'{url}'), None)
                if not url_info:
                    resp = make_response(jsonify({"message": "url not found"}),404)
                    resp.headers["Content-Type"] = "application/json"
                    return resp
                else:
                    resp = make_response(jsonify(url_info),200)
                    resp.headers["Content-Type"] = "application/json"
                    return resp                   
            except Exception as exception:
                return jsonify(str(exception))
        else:
            resp = make_response(jsonify({"message": "Please provide host and parameters in base64"}),400)
            resp.headers["Content-Type"] = "application/json"
            return resp

    else:
        resp = make_response(jsonify({"message": "Bad request"}),400)
        resp.headers["Content-Type"] = "application/json"
        return resp



@app.route('/urlinfo/<int:version>/<url>', methods=["POST"])
def post_url(version, url):
    """Function to Add a URL to the API"""

    verified = request.args.get('verified')

    if version == 1 and url and verified and request.method == "POST":

        if isBase64(url):
            try:
                #Add URL
                url = { 'id': next(id), 
                        'base64_url': url, 
                        'verified': verified, 
                        'verified_at': datetime.utcnow() 
                }
                URLS.append(url)
                resp = make_response(jsonify(url),201)
                resp.headers["Content-Type"] = "application/json"
                return resp
            except Exception as exception:
                return jsonify(str(exception))
        else:
            resp = make_response(jsonify({"message": "Please provide host and parameters in base64"}),400)
            resp.headers["Content-Type"] = "application/json"
            return resp

    else:
        resp = make_response(jsonify({"message": "Bad request"}),400)
        resp.headers["Content-Type"] = "application/json"
        return resp


def isBase64(s):
    try:
        return base64.b64encode(base64.b64decode(s)).decode() == s
    except Exception:
        return False
