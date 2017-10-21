from wtforms import Form, fields, validators

from app.models import db, User
import ipdb

class RegistrationForm(Form):
    email = fields.StringField('email', [validators.DataRequired(), validators.Email()])
    password = fields.PasswordField('password', [validators.DataRequired()])
    password_confirmation = fields.PasswordField('password_confirmation', [
        validators.DataRequired(),
        validators.EqualTo('password', message='Does\'t match password')
    ])


    def submit(self):
        """ Perform registration """
        if not self.validate(): return False
        try:
            user = User(email=self.email.data, password=self.password.data)
            ipdb.set_trace()
            db.session.add(user)
            db.session.commit()
            self.obj = user
            return True
        except:
            return False
