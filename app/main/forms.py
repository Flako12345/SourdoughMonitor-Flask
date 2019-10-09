from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateTimeField
from wtforms.validators import DataRequired
from datetime import datetime
from flask_table import Table, Col, BoolCol


#########################
###### Form Models ######
#########################





class FeedForm(FlaskForm):

    feedTime = DateTimeField(label='Feedtime')#, #validators=[DataRequired()], default=datetime.utcnow())
    # sourdough = StringField(label='Sourdough', validators=[DataRequired()]) #not the way it should be implemented. Need to be able to choose sourdough to feed
    submit = SubmitField(label='Feed sourdough')

class BakeForm(FlaskForm):
    pass


class SourdoughForm(FlaskForm):
    sourdough_name = StringField(label='Name', validators=[DataRequired()])
    birthday = DateTimeField(label='Birthday', default=datetime.utcnow())
    create = SubmitField(label='Spawn!')



###########################
###### Table Models #######
###########################


class SourdoughTable(Table):
    name = Col('Sourdough')
    birthday = Col('Birthday')
    alive = BoolCol('Alive', yes_display='Yes', no_display='No')
    id = Col('Id')

class FeedTable(Table):
    id = Col('Feeding Id')
    timestamp = Col('Feeding Time')
    sourdoughName = Col('Sourdough', attr_list=['sourdough','name'])


class ReadingTable(Table):
    id = Col('Reading ID')
    timestamp = Col('Reading Time')
    reading = Col('Reading')
    sourdoughName = Col('Sourdough', attr_list=['sourdough', 'name'])