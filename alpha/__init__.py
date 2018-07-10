from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
# stop cookie interference
app.config['SECRET_KEY'] = 'd9e5d161aea7bdaae66380655b0334a7'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
db = SQLAlchemy(app)
from alpha import routes
