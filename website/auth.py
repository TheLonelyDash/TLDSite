from xmlrpc.client import boolean
from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)                  #Set up blueprint for the application

@auth.route('/login')                               #Creates/login for a login page
def login():
    return render_template("login.html")

@auth.route('/logout')                              #Creates/logout for a logout page
def logout():
    return "<p> Logout </p>"

@auth.route('/sign-up')                             #Creates /sign-up for a sign-up page
def sign_up():
    return render_template("sign_up.html")