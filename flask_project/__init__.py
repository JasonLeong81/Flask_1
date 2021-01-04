from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db'

    DB.init_app(app) # associate databse with app (so now there's a connection between them)

    from .views import main
    app.register_blueprint(main)


    return app

# set FLASK_APP=flask_project
# flask run 