from flask import Flask, render_template, request, url_for, flash, redirect, render_template_string
from crime_pathfinder import app
from crime_pathfinder.forms import MapForm
from crime_pathfinder.map_utils import get_df, get_map
import json
import plotly
import plotly.express as px
import pandas as pd
from crime_pathfinder.texttolonlat import geocode_address
from crime_pathfinder import datalist
# app = Flask(__name__)
app.config['SECRET_KEY'] = 'df0331cefc6c2a9a5d0208a726a5d1c0fd17324feba25506'

@app.route('/', methods=('GET', 'POST'))
def index():
    form = MapForm()
    print(datalist)
    if request.method == "POST" and form.validate_on_submit():
        flash('Map data submitted succesfully!', 'success')
        categories = form.categories.data
        times_of_day = form.times_of_day.data
        df = get_df(2024,categories=categories,times_of_day=times_of_day)
        fig = get_map(df)
        div = fig.to_html(full_html=False)
        return render_template_string('''
            <head>
            <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>    
            </head>
            <body>
            {{ div_placeholder|safe }}
            </body>''', div_placeholder=div)
    return render_template('register.html', title='Register', form=form)

    # fig.show()

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
