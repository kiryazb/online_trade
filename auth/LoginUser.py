from flask_login import UserMixin

from auth.models import User


# class LoginUser(UserMixin):
#     def __init__(self, user_id, username, password):
#         self.id = user_id
#         self.username = username
#         self.password = password
#
#     @staticmethod
#     def get(user_id):
#         return User.query.get(int(user_id))
#
#     def get_id(self):
#         return str(self.id)
#
#     def __str__(self):
#         return f'<users {self.id}>'
#
#
#     def is_authenticated(self):
#         return True