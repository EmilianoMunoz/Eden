from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
import os 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)

    load_dotenv()
    
    app.config['SQLALCHEMY_DATABASE_URI'] = print(os.environ.get('FULL_URL_DB'))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    migrate = Migrate()
    migrate.init_app(app,db)

    return app