from flask import Blueprint, render_template

main_page = Blueprint('main_page', __name__,
                      template_folder='templates', static_folder='static',
                      static_url_path='/static/main_page')


@main_page.route('/')
def index():
    return render_template("main_page/index.html")
