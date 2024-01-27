from flask import Flask, render_template, request, url_for, flash, redirect
from crime_pathfinder import app
from crime_pathfinder.forms import RegistrationForm

# app = Flask(__name__)
app.config['SECRET_KEY'] = 'df0331cefc6c2a9a5d0208a726a5d1c0fd17324feba25506'

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

@app.route('/')
def index():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

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
