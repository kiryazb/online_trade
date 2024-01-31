from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import InputRequired

class OfferForm(FlaskForm):
    description_want = StringField("Описание: ", validators=[InputRequired()])
    image_want = FileField('Выберите изображение', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Только изображения разрешены')])
    description_have = StringField("Описание: ", validators=[InputRequired()])
    image_have = FileField('Выберите изображение', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Только изображения разрешены')])
    submit = SubmitField("Выставить")
