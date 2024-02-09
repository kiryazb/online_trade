import os
from flask import Flask, render_template
from flask_login import LoginManager

from main_page.views import main_page, socketio
from auth.views import auth, login_manager

from flask_socketio import SocketIO

from flask_sqlalchemy import SQLAlchemy

from database import db
from settings import DATABASE, SECRET_KEY
from trade.views import trade

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
login_manager.init_app(app)

app.register_blueprint(main_page)
app.register_blueprint(auth)
app.register_blueprint(trade)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE

app.config['SECRET_KEY'] = SECRET_KEY

socketio.init_app(app)


def main():
    from auth.models import User
    from trade.models import TradeOffer
    db.init_app(app)

    with app.app_context():
        db.create_all()

    socketio.run(app, allow_unsafe_werkzeug=True)


if __name__ == "__main__":
    main()
