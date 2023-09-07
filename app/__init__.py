from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    load_dotenv()

    # db_user = os.environ.get('USER_DB')
    # db_pass = os.environ.get('PASS_DB')
    # db_url = os.environ.get('URL_DB')
    # db_name = os.environ.get('NAME_DB')

    # app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_pass}@{db_url}/{db_name}'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('FULL_URL_DB')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)


    from app.resources import home
    from app.resources import cliente

    app.register_blueprint(home, url_prefix = '/api/v1')
    app.register_blueprint(cliente, url_prefix = '/api/v1/cliente')



    return app
