import models
from flask import render_template
from flask.views import MethodView

class Index(MethodView):
    '''Index presenter, handles relationship for model and index view'''
    def __init__(self):
        self.model = models.get_model()
        self.template = 'index.html'

    def get(self):
        keys = [ 'quote', 'name', 'year']
        entries = [dict(zip(keys, value)) for value in self.model.read()]
        print(entries)
        return render_template(self.template, entries=entries)
