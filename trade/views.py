from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

from database import db
from trade.forms import OfferForm
from trade.models import TradeOffer

trade = Blueprint('trade', __name__, template_folder='templates', static_folder='static',
                  static_url_path='/static/trade')


@trade.route('/offer', methods=["POST", "GET"])
@login_required
def create_offer():
    form = OfferForm()
    if request.method == "POST":
        if form.validate_on_submit():
            try:
                description_want = request.form['description_want']
                image_want = request.files['image_want']
                description_have = request.form['description_have']
                image_have = request.files['image_have']
                offer = TradeOffer(description_want=description_want, image_want=image_want.read(),
                                   description_have=description_have,
                                   image_have=image_have.read(), user=current_user)
                db.session.add(offer)
                db.session.commit()
                flash("Предложение успещно создано", category="success")
                return redirect(url_for('main_page.index'))
            except:
                db.session.rollback()
                flash("Ошибка при обработке предложения", category="error")
        else:
            flash('Введены некорректные данные', category="error")
    return render_template("trade/create_offer.html", form=form)
