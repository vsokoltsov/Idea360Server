from . import Resource, request
from app.forms import RegistrationForm
import ipdb

class RegistrationsResource(Resource):
    """ Registration resource """

    def post(self):
        """ receive user params and create a new user """
        
        form = RegistrationForm(data=request.get_json())
        if form.submit():
            return { 'token': str(form.token) }, 201
        else:
            return { 'errors': form.errors }, 400
