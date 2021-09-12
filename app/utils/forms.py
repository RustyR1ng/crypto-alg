from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, TextAreaField
from lib_crypto import get_algs


class EncForm(FlaskForm):
    crypto_algs = get_algs().keys()
    select_choices = {alg: alg for alg in crypto_algs}

    alg = SelectField("Алгоритм", choices=select_choices)
    key = StringField("Ключ")
    text = TextAreaField(render_kw={"placeholder": "Текст"})
    enc = SubmitField("Зашифровать")
    dec = SubmitField("Расшифровать")

    def get_data(self):

        switch = "enc" if self.enc.data else "dec"
        data = [self.alg.data, self.text.data, self.key.data, switch]

        return data
