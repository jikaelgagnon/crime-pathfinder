from flask import Flask
import os

# this file causes this folder to act as a package, making imports easier
app = Flask(__name__)
app.app_context().push() # Needed to create db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

from crime_pathfinder import routes