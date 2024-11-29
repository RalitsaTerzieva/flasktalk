from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from puppycompanyblog import db
from puppycompanyblog.models import User, BlogPost
from puppycompanyblog.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from puppycompanyblog.users.picture_handler import add_profile_pic


users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user:
            flash('Email already registered!')
            return redirect(url_for('users.register'))
        
        new_user = User(email=form.email.data, username=form.username.data, password=form.password.data)

        db.session.add(new_user)
        db.session.commit()
        flash('Thanks for registration!')

        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)


@users.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You logged out!')
    return redirect(url_for('core.index'))