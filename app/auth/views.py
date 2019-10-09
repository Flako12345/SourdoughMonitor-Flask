from flask import render_template, url_for, redirect, flash
from flask_login import current_user, login_required, login_user, logout_user
from .. import db
from . import forms
from ..models import User
from . import auth




@auth.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = forms.LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('.login'))
        login_user(user)
        return redirect(url_for('main.index'))
    return(render_template("auth/login.html", form=form))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out. We look forward to see you make more sourdough.')
    return redirect(url_for('main.index'))

