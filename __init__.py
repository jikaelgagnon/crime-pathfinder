from flask import Flask

# this file causes this folder to act as a package, making imports easier
app = Flask(__name__)

from crime_pathfinder import routes