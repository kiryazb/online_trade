from flask_login import UserMixin

from database import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(500), unique=True)

    def __str__(self):
        return f'<users {self.id}>'

    @staticmethod
    def get(user_id):
        return User.query.get(int(user_id))

    def get_id(self):
        return str(self.id)

    def is_authenticated(self):
        return True
