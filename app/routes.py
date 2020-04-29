#this file stores all the view functions for each page a user will visit

from app import app
from app.forms import LoginForm, RegistrationForm, PhotoForm
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user, login_user, logout_user
from flask import request, render_template, flash, redirect, url_for

#functions when visiting homepage
@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
@login_required
#functions here
def home():
    form = PhotoForm()
    if form.validate_on_submit():
        f = form.photo.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(
            app.instance_path, 'photos', filename))
    return render_template('home.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    #if form passes all validators
    if form.validate_on_submit():
        #code to query db for user here
        #code to flash error if no user by name or incorrect password
        #if all of the above pass, log user in
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != "":
            #then redirect to homepage using name of view function
            next_page =url_for('home')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
@login_required
def logout():
        logout_user()
        return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        form = RegistrationForm()
        if form.validate_on_submit():
            #code to add user to database goes here
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('home'))
        return render_template('register.html', title='Register', form=form)
    
@app.route('/<username>/history')
@login_required
def history():
        #code for displaying previous conversions goes here
    return render_template('history.html')

@app.route('/results')
@login_required
def results():
        #code for displaying conversion and summary here
    return render_template('results.html')