from flask import Flask, render_template
from crime_pathfinder import app

@app.route('/')
def home():
    return '<h1>Penis</h1>'