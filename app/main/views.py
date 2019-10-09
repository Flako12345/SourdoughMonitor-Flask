#from app import app
from flask import render_template, url_for, redirect, flash
from flask_login import current_user, login_user, login_required
from .. import db
from . import forms
from ..models import User, Sourdough, Feeding, Reading
from . import main

"""
@main.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = forms.LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('.login'))
        login_user(user)
        return redirect(url_for('.index'))
    return(render_template("login.html", form=form))
"""

@main.route("/")
@main.route("/index", methods=['GET'])
@login_required
def index():
    return render_template("index.html")

@main.route("/sourdoughs", methods=['GET','POST'])
@login_required
def sourdoughs():
    form = forms.SourdoughForm()
    table = forms.SourdoughTable(current_user.sourdoughs.all(), no_items="We don't have any!", classes=['table', 'table-dark'])
    if form.validate_on_submit():
        sourdough = Sourdough(name=form.sourdough_name.data, user = current_user)
        db.session.add(sourdough)
        db.session.commit()
        flash("{name} has been spawned".format(name=sourdough.name))
        return redirect(url_for('.sourdoughs'))
    return render_template('sourdoughs.html', form=form, table=table)



@main.route("/feedings", methods=['GET'])
@login_required
def feedings():
    sourdoughs = Sourdough.query.all()

    feedings = Feeding.query.all()
    for dough in sourdoughs:
       dough.form = forms.FeedForm()
       dough.lastFed = dough.feedings.order_by(Feeding.timestamp.desc()).first()

           #Feeding.query.filter(sourdough_id == dough.id).first()

       if dough.form.validate_on_submit():
            feeding = Feeding(sourdough = dough, timestamp = dough.form.feedTime.data)
            db.session.add(feeding)
            db.session.commit()
            flash("{sourdough} has been fed!".format(sourdough=dough.name))

    feedTable = forms.FeedTable(feedings, no_items="You haven't feed anything yet! What are you waiting for?",
                                classes=['table', 'table-dark'])
    return render_template('feedings.html', sourdoughs=sourdoughs, feedings=feedings, feedTable=feedTable)


@main.route("/sourdough/<id>/feed", methods=['POST'])
@login_required
def feed(id):
    form = forms.FeedForm()
    if form.validate_on_submit():
        feeding = Feeding(sourdough_id = id) #missing assignment to fields from form
        db.session.add(feeding)
        db.session.commit()
        flash("{sourdough} has been fed!".format(sourdough=feeding.sourdough.name))
    return redirect(url_for('main.feedings'))


@main.route("/readings")
@login_required
def readings():
    readings = Reading.query.all()
    readingTable = forms.ReadingTable(readings, no_items="No readings registered", classes=['table', 'table-dark'])

    return render_template('readings.html', readingTable=readingTable)


"""
Old version of feedings
@app.route("/feedings", methods=['GET','POST'])
@login_required
def feedings():
    sourdoughs = Sourdough.query.all()
    formList = []
    feedings = Feeding.query.all()
    cnt = len(feedings)
    for dough in sourdoughs:
       dough.form = forms.FeedForm()

       if dough.form.validate_on_submit():
            feeding = Feeding(sourdough = dough, timestamp = dough.form.feedTime.data)
            db.session.add(feeding)
            db.session.commit()
            flash("{sourdough} has been fed!".format(sourdough=dough.name))

    feedTable = forms.FeedTable(feedings)
    return render_template('feedings.html', cnt=cnt, sourdoughs=sourdoughs, feedings=feedings, feedTable=feedTable)
    
"""


