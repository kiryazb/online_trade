from flask_login import UserMixin

from database import db


class TradeOffer(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('trade_offers', lazy=True))
    description_want = db.Column(db.String(100), unique=True)
    image_want = db.Column(db.LargeBinary)
    description_have = db.Column(db.String(100), unique=True)
    image_have = db.Column(db.LargeBinary)

    def __str__(self):
        return f'<offer: {self.id}>'
