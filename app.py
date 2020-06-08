# importing stuff
from flask import Flask
from flask import request
from flask import jsonify
import json
# importing flask mysqldb
from flask_mysqldb import MySQL

from flask_cors import CORS
import os
import uuid
from werkzeug.utils import secure_filename
# importing pyrebase
import pyrebase

# temp uploads
UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}


# filter for the mime-types
def allowed_files(filename):  # this takes the last part of the file and checks if the format is allowed
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)
# config
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQ_DB"] = "flaskposts"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
mysql = MySQL(app)
CORS(app)

# firebase config
config = {
    "apiKey": "AIzaSyDvjC8YsothLL2H_Bog7frNIpHfGBQO9NQ",
    "authDomain": "post-web-application-1.firebaseapp.com",
    "databaseURL": "https://post-web-application-1.firebaseio.com",
    "projectId": "post-web-application-1",
    "storageBucket": "post-web-application-1.appspot.com",
    "messagingSenderId": "258952961154",
    "appId": "1:258952961154:web:a4cebbf92c0d309888a89b",
    "measurementId": "G-054V5S2V16",
    "serviceAccount": "keyfile.json"
}

# init firebase app
firebase = pyrebase.initialize_app(config)
# firebase storage
storage = firebase.storage()


@app.route("/api/posts", methods=["GET"])  # this handles get requests only
def index():
    if request.method == "GET":
        return jsonify(data="posts main response")


# doesn't work the way it was supposed to
# @app.route("/api/addpost", methods=["POST"]) #this handles post requests only
# def index2():
#     if request.method =="POST":
#         return jsonify(data="THIS IS SO COOL ACTUALLY")


@app.route("/api/addpost", methods=["POST"])
def index():
    if (request.method == "GET"):
        return jsonify(data="posts main response")


@app.route("/api/addpost", methods=["GET"])
def addpost():
    if (request.method == "POST"):
        print(request.form, flush=True)

        title = request.form.get("title")
        content = request.form.get("content")
        cover = request.files["cover"]

        if cover and allowed_files(cover.filename):
            filename = str(uuid.uuid4())
            filename += "." + cover.filename.split(".")[1]
            # create secure name
            filename_secure = secure_filename(filename)
            # save the file inside the uploads folder
            cover.save(os.path.join(app.config["UPLOAD_FOLDER"], filename_secure))
            # local file
            local_filename = "./uploads/"
            local_filename += filename_secure
            # firebase file_name
            firebase_filename = "uploads/"
            firebase_filename += filename_secure
            # uploading the file
            storage.child(firebase_filename).put(local_filename)
            # getting the url of the file
            cover_image = storage.child(firebase_filename).get_url(None)
            # getting the cursor to execute the mysql functions
            cur = mysql.connection.cursor()
            cur.execute(""" INSERT INTO flaskposts (title, content, cover, covername) VALUES(%s, %s, %s, %s) """,
                        (title, content, cover_image, filename_secure))
            os.remove(os.path.join(app.config["UPLOAD_FOLDER"], filename_secure))  # removing the file that we created
            return jsonify(data = "The Post was Created Successfully")



if __name__ == "__main__":
    app.run(debug=True)
