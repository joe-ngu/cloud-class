import models
from flask import render_template, redirect, url_for
from flask.views import MethodView

class Index(MethodView):
    '''Index presenter, handles relationship for model and index view'''
    def __init__(self):
        self.model = models.get_model()
        self.template = 'index.html'

    def get(self):
        '''Function to get all foods currently being tracked and render them on html'''
        keys = ['name', 'calories', 'fat', 'carbs', 'protein', 'quantity']
        foods = [dict(zip(keys, value)) for value in self.model.read()]
        return render_template(self.template, foods=foods)

    def post(self):
        '''Function to delete all food items from list. Because html method tags don't support delete methods
        This was a work around that I used to delete the items from my list.'''
        self.model.delete()
        return redirect(url_for('index'))
