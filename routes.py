from flask import Flask, request, Response, jsonify
from flask_cors import CORS, cross_origin
from flask import Flask, make_response
from scraper.scraper import get_profile, scrape
import json
app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/api/palettes', methods=['GET'])
@cross_origin()
def get_tasks():
    user = request.args.get('user')
    print("User: ", user)
    print(request.headers)
    print("~~~~~~~~~~~")
    try:
        response = get_profile(user)
    except:
        return "Record not found", 400
    return jsonify(result=response)


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
