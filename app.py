# importing stuff
from flask import Flask
from flask import request
from flask import jsonify
import json 
# importing flask mysqldb
from flask_cors import CORS
import os
import uuid
from werkzeug.utils import secure_filename
# importing pyrebase


# temp uploads
UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True)