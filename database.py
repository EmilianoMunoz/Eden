from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

db = SQLAlchemy()

USER_DB = 'emiliano'
PASS_DB = '40321766'
URL_DB = 'localhost'
NAME_DB = 'eden'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

load_dotenv()

SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URI')