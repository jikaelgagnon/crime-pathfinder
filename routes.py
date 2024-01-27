from flask import Flask, render_template
from crime_pathfinder import app

@app.route('/')
def home():
    

@app.route('/map')
def map():
    return render_template('map.html')

