
from .base import Model
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

class QuotesModel(Model):
    def __init__(self):
        self.client = datastore.Client('cloud-nguyen-jtn7')

    def select(self):
        query = self.client.query(kind = 'Quotes')
        entities = list(map(from_datastore, query.fetch()))

    def insert(self, quote, name, year):
        key = self.client.key('Quotes')
        rev = datastore.Entity(key)
        rev.update( {
            'quote': quote,
            'name': name,
            'year': year
        })
        self.client.put(rev)
        return True


