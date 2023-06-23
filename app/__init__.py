from flask import Flask
from flask_migrate import Migrate
from config import Config
from app.views import bp
from app.db import db
from app.models import Employee, Position, Division, Job # noqa


app = Flask(__name__)
app.debug = True
app.config.from_object(Config)

# extensions here
db.init_app(app)
migrate = Migrate(app, db)

# register blueprint here
app.register_blueprint(bp)
