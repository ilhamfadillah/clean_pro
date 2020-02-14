from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Text, DateTime
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(String(255))
    email = db.Column(String(255))
    password_hash = db.Column(String(255))
    access_token = db.Column(Text)
    refresh_token = db.Column(Text)
    created_at = db.Column(DateTime)

    """
    def __init__(self, id, uuid, email,
                 password_hash, access_token, refresh_token, created_at):
        self.id = id
        self.uuid = uuid
        self.email = email
        self.password_hash = password_hash
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.created_at = created_at
    """


    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')


    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


    @classmethod
    def seed(self, fake):
        user = User(
            uuid=str(uuid.uuid4()),
            email=fake.email(),
            password='password',
            created_at=datetime.now(),
        )
        db.session.add(user)
        db.session.commit()
