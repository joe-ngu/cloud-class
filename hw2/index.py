import models
from flask import render_template
from flask.views import MethodView

class Index(MethodView):
    def __init__(self):
        self.model = models.get_model()
        self.template = 'index.html'

    def get(self):
        keys = ['quote', 'name', 'year']
        values = self.model.read()
        entries = [dict(zip(keys, values)) for value in values]
        return render_template(self.template, entries=entries)
