import models
from flask import redirect, request, render_template, url_for
from flask.views import MethodView

class Foods(MethodView):
    '''Foods presenter, handles relationship for models and food view'''
    def __init__(self):
        self.model = models.get_model()
        self.template = 'foods.html'

    def post(self):
        '''
        Accepts POST requests, and processes form;
        Redirect to index when completed.
        '''
        self.model.create(
            request.form['name'],
            request.form['quantity']
        )
        return redirect(url_for('index'))

    def get(self):
        return render_template(self.template) 

    def put(self):
        pass

    def delete():
        pass
