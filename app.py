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

#filter for the mime-types
def allowed_files(filename): # this takes the last part of the file and checks if the format is allowed
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
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    "measurementId": "",
    "serviceAccount": "keyfile.json"
}

#init firebase app
firebase = pyrebase.initialize_app(config)
#firebase storage
storeage = firebase.storage()




@app.route("/api/posts", methods=["GET"]) # this handles get requests only
def index():
    if request.method == "GET":
        return jsonify(data="posts main response")

# doesn't work the way it was supposed to
# @app.route("/api/addpost", methods=["POST"]) #this handles post requests only
# def index2():
#     if request.method =="POST":
#         return jsonify(data="THIS IS SO COOL ACTUALLY")


if __name__ == "__main__":
    app.run(debug=True)