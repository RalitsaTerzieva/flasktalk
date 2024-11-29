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


@users.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Logged in Successfully!")

            next = request.args.get('next')  # Get the next URL the user intended to access before login.
            
            # Validate 'next' or default to home page
            if next is None or next[0] != '/':
                next = url_for('core.index')

            return redirect(next)
        
        flash("Login Unsuccessful. Please check email and password.")
        return render_template('login.html', form=form)

    return render_template('login.html', form=form)


@users.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You logged out!')
    return redirect(url_for('core.index'))


@users.route('/account', methods=['GET','POST'])
@login_required
def account():

    form = UpdateUserForm()

    if form.validate_on_submit():

        if form.picture.data:
            username = current_user.username
            pic = add_profile_pic(form.picture.data, username)
            current_user.profile_image = pic

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('User Account Updated!')
        return redirect(url_for('users.account'))
    
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    
    profile_image = url_for('static', filename='profile_pics/'+current_user.profile_image)
    return render_template('account.html', profile_image=profile_image, form=form)