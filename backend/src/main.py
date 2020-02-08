import os
import sys
from flask import Flask, flash, request, redirect, url_for, escape, Response, send_file
from werkzeug.utils import secure_filename
from pathlib import Path
from zipfile import ZipFile
from db_utils.redis_handler import redis_handler
from process_music.process_music import main as pMain

ALLOWED_EXTENSIONS = {'midi', 'mid'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['PROCESS_FOLDER'] = 'process'
app.config['MAX_CONTENT_LENGTH'] = 40 * 1024 * 1024
app.config['SECRET_KEY'] = os.urandom(24).hex()

app.config['REDIS_HOST'] = 'redis'
app.config['REDIS_PORT'] = 6379
app.config['REDIS_DB'] = 0

redis = redis_handler(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def createZip(processPath):
    zipPath = os.path.join(processPath, "data.zip")
    with ZipFile(zipPath, 'w') as zipObj:
        zipObj.write(os.path.join(processPath, "track_0.csv"))
        zipObj.write(os.path.join(processPath, "track_0.xes"))
        zipObj.write(os.path.join(processPath, "track_0_footprint_matrix.txt"))
    return True

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
    Path(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER'])).mkdir(exist_ok=True)
    Path(os.path.join(os.getcwd(), app.config['PROCESS_FOLDER'])).mkdir(exist_ok=True)
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
            filename = secure_filename(file.filename).split('.')[0]
            uploadPath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            processPath = os.path.join(app.config['PROCESS_FOLDER'], filename)
            if redis.get(filename) is None:
                file.save(uploadPath)
                if not os.path.isdir(processPath):
                    os.mkdir(processPath)
                args = {}
                args["MIDI_FILE"] = uploadPath
                args["--measures"] = 1
                args["--output_dir"] = processPath
                args["--tracks"] = [0]
                pMain(args)
                redis.save({f"{filename}": f"{filename}"})
                createZip(processPath)
                return send_file(os.path.join(os.getcwd(), processPath, "data.zip"), as_attachment=True)
            else:
                createZip(processPath)
                return send_file(os.path.join(os.getcwd(), processPath, "data.zip"), as_attachment=True)
    return Response('{"error": "Only POST requests are allowed."}', status=405, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')