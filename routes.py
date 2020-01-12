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
    response = get_profile(user)
    return jsonify(result=response)
