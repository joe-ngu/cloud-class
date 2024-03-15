import os
import requests
from dotenv import load_dotenv


load_dotenv()

app_key = os.getenv('APP_KEY')
app_id = os.getenv('APP_ID')

base_url = 'https://api.edamam.com/api/'

def get_nutrition(food_name):
    '''
    Gets nutrition for a food by name
    :param food_name:
    :return: dict of nutrition data (calories, fat, carbs, protein) by gram
    '''
    url = base_url + 'nutrition-data'
    params = {
        'ingr': food_name,
        'app_id': app_id,
        'app_key': app_key,
        'nutrition-type': 'logging'
    }
    response = requests.get(url, params=params)
    print(response.url)
    data = response.json()
    data_weight = data['totalWeight']
    calories_per_gram = data['calories'] / data_weight
    fat = data['totalNutrients']['FAT']['quantity'] / data_weight
    carbs = data['totalNutrients']['CHOCDF']['quantity'] / data_weight
    protein = data['totalNutrients']['PROCNT']['quantity'] / data_weight
    extracted_data = {
        'calories_per_gram': calories_per_gram,
        'fat_per_gram': fat,
        'carbs_per_gram': carbs,
        'protein': protein
    }
    return extracted_data
