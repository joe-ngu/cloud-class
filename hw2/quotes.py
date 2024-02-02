import models
from flask import redirect, request, render_template, url_for
from flask.views import MethodView

class Quotes(MethodView):
    '''Quotes presenter, handles relationship for quotes models and views'''
    def __init__(self):
        self.model = models.get_model()
        self.template = 'quotes.html'

    def post(self):
        '''
        Accepts POST requests, and processes form;
        Redirect to index when completed.
        '''
        self.model.insert(request.form['quote'], request.form['name'], request.form['date'])
        return redirect(url_for('index'))

    def get(self):
        return render_template(self.template) 

    def put(self):
        pass

    def delete():
        pass
