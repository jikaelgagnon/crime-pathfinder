from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# this file causes this folder to act as a package, making imports easier
app = Flask(__name__)
app.config['SECRET_KEY'] = 'banana'
app.app_context().push() # Needed to create db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

datalist = []

from crime_pathfinder import routes