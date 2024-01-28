from flask import Flask, render_template, request, url_for, flash, redirect
from datetime import datetime
from crime_pathfinder import app , db , datalist
from flask_sqlalchemy import SQLAlchemy
from crime_pathfinder.database import Incident
from crime_pathfinder.texttolonlat import geocode_address

app.config['SECRET_KEY'] = 'df0331cefc6c2a9a5d0208a726a5d1c0fd17324feba25506'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        crime_1 = request.form['Crime']
        location = request.form['Location']
        description_1 = request.form['Description']
        time_of_day = request.form['Time']

        coordonates = geocode_address('AIzaSyB0OTXJmDBC3Al_FiDhMojWLK9F8Obm5x8', location)
        coordonates_lat = coordonates[0]
        coordonates_long = coordonates[1]


        if not crime_1:
            flash('Crime type is required!')
        elif not location:
            flash('Location is required!')
        else:
            datalist.append({'crime': crime_1, 'description': description_1, 'Latitude': coordonates_lat, 'Longitude': coordonates_long, 'time_of_day': time_of_day})
            return redirect(url_for('index'))
    
    return render_template('create.html')


 #crime_report = Incident(
           # crime_type = crime_1,
           # description = description_1,
           # longitude = coordonates_long,
           # latitude = coordonates_lat
        #)
            
           # db.session.add(crime_report)
           # db.session.commit()