from flask import Flask

def create_app():                                       #Initializes flask
    app = Flask(__name__)
    app.config['SECRED_KEY'] = 'CS@226cs'               #Encrypts cookies and session data for the website

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/' )
    app.register_blueprint(auth, url_prefix = '/' )
    
    return app