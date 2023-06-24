from flask import Flask
from flask_migrate import Migrate
from config import Config
from app.views import bp
from app.db import db
from app.models import Employee, Position, Division, Job # noqa
from app.auth import auth
from flask_login import LoginManager
from app.models import User


app = Flask(__name__)
app.debug = True
app.config.from_object(Config)

# extensions here
db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# register blueprint here
app.register_blueprint(bp)
app.register_blueprint(auth)
