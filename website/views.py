from flask import Blueprint, render_template

views = Blueprint('views', __name__)                #Set up blueprint for the application

@views.route('/')                                   #Function runs when we go to / url
def home():
    return render_template("home.html")