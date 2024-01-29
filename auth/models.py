from database import db

from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(500), unique=True)

    def __init__(self, user_id, username, password):
        self.id = user_id
        self.username = username
        self.password = password


    @staticmethod
    def get(user_id):
        return User.query.get(int(user_id))

    def get_id(self):
        return str(self.id)

    def __str__(self):
        return f'<users {self.id}>'

    def is_authenticated(self):
        return True
