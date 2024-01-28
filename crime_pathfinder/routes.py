from flask import Flask, render_template, request, url_for, flash, redirect, render_template_string
from crime_pathfinder import app
from crime_pathfinder.forms import MapForm
from crime_pathfinder.map_utils import generate_map
import json
import plotly
import plotly.express as px
import pandas as pd
# app = Flask(__name__)
app.config['SECRET_KEY'] = 'df0331cefc6c2a9a5d0208a726a5d1c0fd17324feba25506'

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

@app.route('/', methods=('GET', 'POST'))
def index():
    form = MapForm()
    if request.method == "POST" and form.validate_on_submit():
        flash('Map data submitted succesfully!', 'success')
        categories = form.categories.data
        times_of_day = form.times_of_day.data
        fig = generate_map(2024,categories=categories,times_of_day=times_of_day)
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
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('index'))

    return render_template('create.html')
