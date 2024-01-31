from flask_login import login_user, login_required, LoginManager, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from auth.forms import RegisterForm, LoginForm
from auth.models import User
from flask import Blueprint, render_template, request, flash, redirect, url_for
from database import db

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static', static_url_path='/static/auth')
login_manager = LoginManager()


@auth.route('/register', methods=["POST", "GET"])
def register():
    form = RegisterForm()

    if request.method == "POST" and form.validate_on_submit():
        try:
            hash_password = generate_password_hash(request.form['password'])
            user = User(username=request.form['username'], email=request.form['email'], password=hash_password)
            db.session.add(user)
            db.session.commit()
            flash("Успешная регистрация", category="success")
            return redirect(url_for('auth.login'))
        except:
            db.session.rollback()
            flash("Ошибка при сохранении пользователя в базу данных", category="error")

    return render_template("auth/register_form.html", form=form)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@auth.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()

    if request.method == "POST":
        if form.validate_on_submit():
            username = request.form['username']
            password = request.form['password']

            user = User.query.filter_by(username=username).first()

            if user and check_password_hash(user.password, password):
                login_user(user, remember=form.remember.data)
                return redirect(url_for("auth.profile", username=username))
            else:
                flash('Неверное имя пользователя или пароль', category="error")
        else:
            flash('Введены некорректные данные', category="error")

    return render_template("auth/login_form.html", form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы успешно вышли из аккаунта', 'success')
    return redirect(url_for('main_page.index'))


@auth.route('/user/<username>')
@login_required
def profile(username):
    if current_user.username != username:
        return redirect(url_for('auth.profile', username=current_user.username))

    return render_template("auth/profile.html", username=username)
