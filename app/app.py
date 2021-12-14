from flask import jsonify, make_response, request, Flask
import base64


app = Flask(__name__)


URLS = [
  { 'id': '1', 'base64_url': 'd3d3Lmdvb2dsZS5jb20vc2VhcmNoP3E9dXJpJmNsaWVudD11YnVudHUmaHM9Um5UJmNoYW5uZWw9ZnMmc3hzcmY9QU9hZW12SXotN1hjQVpHamY0V0F6Tmc4VjRSUkx6dGl5QToxNjM5NDc4NzUwNTI2JnRibT1pc2NoJnNvdXJjZT1pdSZpY3R4PTEmZmlyPVZ5Q1VJWGNSVjN2aWFNJTI1MkNfYlh0eGhoRTRjWG84TSUyNTJDJTI1MkZtJTI1MkYwN3d6MiUyNTNCMlZPNE5jdlFoN0VzQk0lMjUyQ040RWJMZ21zOFhyVmVNJTI1MkNfJTI1M0JCRU1UemVRWHpIYy03TSUyNTJDSmNVUFdaeFNfWkpLWE0lMjUyQ18lMjUzQlJ5WjExdkdEbXF0WTJNJTI1MkN1NndCTTRtR2UxbEpRTSUyNTJDXyUyNTNCTzFkM3JxRlcyVFkxbU0lMjUyQzVfSzEzREEtWktVSHRNJTI1MkNfJnZldD0xJnVzZz1BSTRfLWtSa1lMa2FvSmxPV2lPc3Y5bDFEaWswYnA3UldBJnNhPVgmdmVkPTJhaFVLRXdpSXhhcWtqdVAwQWhXRFRHd0dIVE5vQ2VnUV9CMTZCQWd0RUFFI2ltZ3JjPVJ5WjExdkdEbXF0WTJN', 'verified': True, 'verified_at': '' }
]

@app.route('/urlinfo/<int:version>/<url>', methods=["GET"])
def get_url(version, url):
    """Function to retreive a URL from the API"""

    if version and url and request.method == "GET":

        if isBase64(url):
            try:
                #Get URL here
                url_info = next((item for item in URLS if item["base64_url"] == f'{url}'), None)
                print(url_info)
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
        resp = make_response(jsonify({"message": "Please provide version, host and params"}),400)
        resp.headers["Content-Type"] = "application/json"
        return resp


def isBase64(s):
    try:
        return base64.b64encode(base64.b64decode(s)).decode() == s
    except Exception:
        return False
