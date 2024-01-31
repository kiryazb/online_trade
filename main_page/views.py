import base64

from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

from trade.models import TradeOffer

main_page = Blueprint('main_page', __name__,
                      template_folder='templates', static_folder='static',
                      static_url_path='/static/main_page')


@main_page.route('/', methods=['GET', 'POST'])
def index():
    offers = TradeOffer.query.all()
    image_list_want = []
    image_list_have = []
    for img in offers:
        image = base64.b64encode(img.image_want).decode('ascii')
        image_list_want.append(image)
        image = base64.b64encode(img.image_have).decode('ascii')
        image_list_have.append(image)

    if request.method == "POST":
        print("dfdfdf")
    return render_template("main_page/index.html", offers=offers,
                           image_list_want=image_list_want, image_list_have=image_list_have, len=len(offers))
