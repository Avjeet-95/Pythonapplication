from fileinput import filename
#import app as app
from flask import Flask,render_template,request,session,redirect,flash,send_file
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import mysql
from werkzeug.utils import secure_filename
import json
import os
from io import BytesIO
import math
with open('config.json','r') as c:
    params=json.load(c)["params"]
local_server=True
app = Flask(__name__)
app.secret_key = 'super-secret-key'

app.config['UPLOAD_FOLDER']=params['upload_location']
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)
class uploadfile(db.Model):
    '''
    sno,name,phone_num,msg,date,email
    '''
    Id = db.Column(db.Integer, primary_key=True)
    File = db.Column(db.String(200))
    Data = db.Column(db.String(200))
class uploadimg(db.Model):
    Id=db.Column(db.Integer, primary_key=True)
    image=db.Column(db.String(200))
@app.route("/")
def upload():
    return render_template('file_upload.html')
@app.route("/uploader",methods=['GET','POST'])
def uploader():
        if(request.method=='POST'):
            file = request.files['file11']
            entry = uploadfile(File=file.filename, Data=file)
            db.session.add(entry)
            db.session.commit()
            flash("File uploaded successfully","success")
        return redirect('/')

if __name__=="__main__":
    app.run()
