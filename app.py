from flask import Flask, redirect, url_for
from auth.auth import auth_bp
from admin.admin import admin_bp
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
db.init_app(app)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.unauthorized_handler
def unauthorized():
    return redirect('/login')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

from model.user_model import User
migrate = Migrate(app, db)

app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)

@app.cli.command('seeder')
def seed():
    from faker import Faker

    fake = Faker()
    for x in range(3):
        User.seed(fake)