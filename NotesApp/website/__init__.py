# website/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db= SQLAlchemy()
DB_NAME = "database.db"

def create_app(): 
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'minotaurthegreat'  # for security and encryption
    # Additional configuration and setup can be added here
    app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{DB_NAME}' #database is stored or located here
    #the database is stored in the website folder, we jut telling flask where
    db.init_app(app) #we tell the database that this is the app we gonna use
   
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    
    with app.app_context():
        db.create_all()
        
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app





