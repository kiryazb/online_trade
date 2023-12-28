import os
from flask import Flask, render_template
from main_page.views import main_page

from flask_sqlalchemy import SQLAlchemy

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
app.register_blueprint(main_page)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:070405@localhost:5432/online_trade'
db = SQLAlchemy(app)


class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    app.run(debug=True)
