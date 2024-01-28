from flask import Flask, render_template, request, url_for, flash, redirect, render_template_string
from crime_pathfinder import app
from crime_pathfinder.forms import MapForm
from crime_pathfinder.map_utils import get_df, get_map, add_row
import json
import plotly
import plotly.express as px
import pandas as pd
from crime_pathfinder.texttolonlat import geocode_address
# app = Flask(__name__)
app.config['SECRET_KEY'] = 'df0331cefc6c2a9a5d0208a726a5d1c0fd17324feba25506'

@app.route('/', methods=('GET', 'POST'))
def index():
    form = MapForm()
    if request.method == "POST" and form.validate_on_submit():
        categories = form.categories.data
        times_of_day = form.times_of_day.data
        start_location = form.start_location.data
        end_location = form.end_location.data

        print(app.config['User reported'])

        df = get_df(2024,categories=categories,times_of_day=times_of_day)
        if 'User reported' in categories:
            for report in app.config['User reported']:
                df = add_row(df, category='User reported', latitude=report['Latitude'], longitude=report['Longitude'])
        if start_location:
            lati, longi = geocode_address(start_location)
            df = add_row(df, category='Start location', latitude=lati, longitude=longi)

        if end_location:
            lati, longi = geocode_address(end_location)
            df = add_row(df, category='End location', latitude=lati, longitude=longi)

        fig = get_map(df)
        # div = fig.to_html(full_html=False)
            # Create graphJSON
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        
        # Use render_template to pass graphJSON to html
        return render_template('map_display.html', graphJSON=graphJSON)
        # return render_template_string('''
        #     <head>
        #     <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>    
        #     </head>
        #     <body>
        #     {{ div_placeholder|safe }}
        #     </body>''', div_placeholder=div)
    return render_template('create_map.html', title='Create a map', form=form)

    # fig.show()

@app.route('/create/', methods=('GET', 'POST'))
def create_report():
    if request.method == 'POST':
        crime_1 = request.form['Crime']
        location = request.form['Location']
        description_1 = request.form['Description']
        time_of_day = request.form['Time']

        coordonates = geocode_address(location)
        coordonates_lat = coordonates[0]
        coordonates_long = coordonates[1]


        if not crime_1:
            flash('Crime type is required!')
        elif not location:
            flash('Location is required!')
        else:
            app.config['User reported'].append({'crime': crime_1, 'description': description_1, 'Latitude': coordonates_lat, 'Longitude': coordonates_long, 'time_of_day': time_of_day})
            return redirect(url_for('index'))
    
    return render_template('create_report.html')
