from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Length, Email, EqualTo


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

    
class MapForm(FlaskForm):
    # categories_fr = ['Introduction','Vol dans / sur véhicule à moteur','Vol de véhicule à moteur','Méfait','Vol qualifié','Infraction entraînant la mort']
    categories_en = ['Breaking and entering','Theft from a vehicle/theft of vehicle parts','Vehicle theft','General damages','Theft with violence','Murder','User reported']
    times_of_day_en = ['Day','Evening','Night']
    year_min = 2015
    year_max = 2025
    categories = MultiCheckboxField(label='Categories', choices=categories_en)
    times_of_day = MultiCheckboxField('Times of Day', choices=times_of_day_en)
    start_location = StringField(label='Start location')
    end_location = StringField(label='End location')
    submit = SubmitField("Submit Data")