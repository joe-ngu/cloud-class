from .base import FoodsBaseModel
from google.cloud import datastore

def from_datastore(entity):
    """Translates Datastore results into the format expected by the
    application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]

    This returns:
        [ name, calories, fat, carbs, protein, quantity ]
    where quote and name are Python strings
    and where year is a Python integer
    """

    if not entity:
        return None
    if isinstance(entity, list):
        entity = entity.pop()
    return [entity['name'],entity['calories'],entity['fat'],entity['carbs'],entity['protein'],entity['quantity']]

class FoodsModel(FoodsBaseModel):
    def __init__(self):
        self.client = datastore.Client('cloud-nguyen-jtn7')

    def read(self):
        query = self.client.query(kind = 'Foods')
        entities = list(map(from_datastore, query.fetch()))
        return entities

    def create(self, name, calories, fat, carbs, protein, quantity):
        key = self.client.key('Foods')
        rev = datastore.Entity(key)
        rev.update( {
            'name': name,
            'calories': calories,
            'fat': fat,
            'carbs': carbs,
            'protein': protein,
            'quantity': quantity
        })
        self.client.put(rev)
        return True

    def delete(self):
        query = self.client.query(kind = 'Foods')
        entities = list(query.fetch())
        for entity in entities:
            self.client.delete(entity.key)


