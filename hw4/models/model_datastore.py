from .base import BaseModel
from google.cloud import datastore

def from_datastore(entity):
    """Translates Datastore results into the format expected by the
    application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]

    This returns:
        [ quote, name, year ]
    where quote and name are Python strings
    and where year is a Python integer
    """

    if not entity:
        return None
    if isinstance(entity, list):
        entity = entity.pop()
    return [entity['quote'],entity['name'],entity['year']]

class QuotesModel(BaseModel):
    def __init__(self):
        self.client = datastore.Client('cloud-Nguyen-jtn7')

    def read(self):
        query = self.client.query(kind = 'Quotes')
        entities = list(map(from_datastore, query.fetch()))
        return entities

    def create(self, quote, name, year):
        key = self.client.key('Quotes')
        rev = datastore.Entity(key)
        rev.update( {
            'quote': quote,
            'name': name,
            'year': year
            })
        self.client.put(rev)
        return True


