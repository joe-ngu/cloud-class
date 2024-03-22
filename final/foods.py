import models
from flask import redirect, request, render_template, url_for
from flask.views import MethodView
from nutrition_api import get_nutrition_info

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

        # api call to get nutrition info
        food_name = request.form['name']
        nutrition_info = get_nutrition_info(food_name)

        # given quantity, compute calories and macro-nutrients
        quantity = int(request.form['quantity'])
        calories_per_gram = nutrition_info['calories_per_gram']
        fat_per_gram = nutrition_info['fat_per_gram']
        carbs_per_gram = nutrition_info['carbs_per_gram']
        protein_per_gram = nutrition_info['protein_per_gram']

        total_calories = round(quantity * calories_per_gram, 2)
        total_fat = round(quantity * fat_per_gram, 2)
        total_carbs = round(quantity * carbs_per_gram, 2)
        total_protein = round(quantity * protein_per_gram, 2)

        # create food item for datastore
        self.model.create(
            name=food_name,
            calories=total_calories,
            fat=total_fat,
            carbs=total_carbs,
            protein=total_protein,
            quantity=quantity
        )
        return redirect(url_for('index'))

    def get(self):
        return render_template(self.template) 