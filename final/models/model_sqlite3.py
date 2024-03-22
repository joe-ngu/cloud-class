
import sqlite3
from .base import FoodsBaseModel

DB_FILE = 'foods.db'

class FoodsModel(FoodsBaseModel):
    '''Foods model for our sqlite database.'''

    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute( 
            '''CREATE TABLE IF NOT EXISTS foods (
                name TEXT,
                calories FLOAT,
                fat FLOAT,
                carbs FLOAT,
                protein FLOAT,
                quantity FLOAT
            )'''
        )
        cursor.close()

    def create(self, name, calories, fat, carbs, protein, quantity):
        '''
        Inserts quote entry into database
        :param name: String
        :param calories: Float
        :param fat: Float
        :param carbs: Float
        :param protein: Float
        :param quantity: Float
        :return: True
        :raises: Database errors on connection and insertion
        '''
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        params = {'name': name, 'calories': calories, 'fat': fat, 'carbs': carbs, 'protein': protein, 'quantity': quantity} 
        cursor.execute(
            f'''INSERT INTO foods (name, calories, fat, carbs, protein, quantity) 
                VALUES (:name, :calories, :fat, :carbs , :protein, :quantity)'''
                , params)

        connection.commit()
        cursor.close()
        return True

    def read(self):
        '''
        Gets all rows from the database
        Each row contains: rowid, quote, name, year
        :return: List of lists containing all rows of database
        '''
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute('''
            SELECT 
                rowid, 
                name, 
                ROUND(calories, 2), 
                ROUND(fat, 2), 
                ROUND(carbs, 2),
                ROUND(protein, 2),
                quantity 
            FROM foods
        ''')
        return cursor.fetchall()
