from app.config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder="templates")
app.config.from_object(Config)
db = SQLAlchemy(app)


from app.static.models import author
from app.static.models import book
