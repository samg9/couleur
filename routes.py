from flask import Flask, request, Response, jsonify, redirect, url_for, session
from flask_cors import CORS, cross_origin
from flask import Flask, make_response
from scraper.scraper import get_profile, scrape
from werkzeug.utils import secure_filename
import json
import os

app = Flask(__name__)

UPLOAD_FOLDER = './'
cors = CORS(app)
app.config.from_envvar('APP_SETTINGS')
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = app.config['DEFAULT_APP_KEY']

# file upload 
@app.route('/api/upload', methods=['POST'])
@cross_origin()
def fileUpload():
    try:
        target=os.path.join(UPLOAD_FOLDER,'test_docs')
        if not os.path.isdir(target):
            os.mkdir(target)
        file = request.files['file']
        filename = secure_filename(file.filename)
        destination="/".join([target, filename])
        file.save(destination)
        session['uploadFilePath']=destination
        return jsonify({"success msg"})
    except Exception as e:
        print("error: ",e)
        return "Unable to upload", 404   

@app.route('/api/palettes', methods=['GET'])
@cross_origin()
def get_tasks():
    user = request.args.get('user')
    pal_size = request.args.get('pal_size')
    print("User: ", user)
    print(request.headers)
    print("~~~~~~~~~~~")
    try:
        response = get_profile(user, pal_size)
    except Exception as e:
        print(e)
        return "Record not found", 400
    return jsonify(result=response)


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=app.config['DEBUG'], threaded=app.config['THREADED'], port=app.conifg['PORT'] ,use_reloader=app.config['USE_RELOADER'])
