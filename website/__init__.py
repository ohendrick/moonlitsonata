from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = 'moonboardapp.db'


def create_app():

    app = Flask(__name__)

    # for encrypting cookies
    app.config['SECRET_KEY'] = 'hjshjh@klkladsf;lkadsfkj;lkdfsi4kdah!jshkjdhjs'

    # configure DB
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # views imports/register
    from website.views.home import home
    app.register_blueprint(home, url_prefix='/')


    return app