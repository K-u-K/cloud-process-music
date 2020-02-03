import os
import sys
from flask import Flask, flash, request, redirect, url_for, escape, Response
from werkzeug.utils import secure_filename
from pathlib import Path
from db_utils.RedisHandler import RedisHandler
from process_music.process_music import main as pMain

UPLOAD_FOLDER = 'uploads/'
OUTPUT_FOLDER = 'output/'
ALLOWED_EXTENSIONS = {'midi', 'mid'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 40 * 1024 * 1024
app.config['SECRET_KEY'] = os.urandom(24).hex()

app.config['REDIS_HOST'] = 'redis'
app.config['REDIS_PORT'] = 6379
app.config['REDIS_DB'] = 0

redis = RedisHandler(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    name = request.args.get("name", "World")
    return '''<!doctype html>
        <title>Upload File</title>
        <h1>Upload File</h1>
        <form action="/upload" method=post enctype=multipart/form-data>
            <input type=file name=file>
            <input type=submit value=Upload>
        </form>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    Path(UPLOAD_FOLDER).mkdir(exist_ok=True)
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return Response('{"error": "No file in POST data found."}', status=400, mimetype='application/json')
        
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return Response('{"error": "Expected name for file in POST data."}', status=400, mimetype='application/json')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            if redis.get(filename) is None:
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                args = {}
                args["MIDI_FILE"] = UPLOAD_FOLDER + filename
                args["--measures"] = 1
                args["--output_dir"] = OUTPUT_FOLDER
                args["--tracks"] = [0]
                pMain(args)
                redis.save({filename: f"{filename}"})
                return Response('{"success": "File ' + filename + ' was successfully uploaded."}', status=200, mimetype='application/json')
            else:
                return Response('{"success": "File ' + filename + ' is already stored. Returning stored data..."}', status=203, mimetype='application/json')
    return Response('{"error": "Only POST requests are allowed."}', status=405, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')