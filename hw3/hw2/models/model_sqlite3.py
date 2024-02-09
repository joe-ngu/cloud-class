'''
Data is stored in a SQLite database that looks something like the following:

+-------+------------------------------+---------+------+
| Rowid | Quote                        | Name    | Year |
+=======+==============================+=========+======+
| 1     | "100 pushups, 100 sit-ups,   | Saitama | 2015 |
|       | 100 squats, and a 10km run!" |         |      |
+-------+------------------------------+---------+------+
'''

import sqlite3
from .base import BaseModel

DB_FILE = 'quotes.db'

class QuotesModel(BaseModel):
    '''Quotes model for our sqlite database.'''

    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute( 
            '''CREATE TABLE IF NOT EXISTS quotes (
                quote TEXT,
                name TEXT,
                year INT
            )'''
        )
        cursor.close()

    def create(self, quote, name, year):
        '''
        Inserts quote entry into database
        :param quote: String
        :param name: String
        :param year: Integer
        :return: True
        :raises: Database errors on connection and insertion
        '''
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        params = {'quote': quote, 'name': name, 'year': year} 
        cursor.execute(
            f'''INSERT INTO quotes (quote, name, year) 
                VALUES (:quote, :name, :year)'''
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
        cursor.execute("SELECT rowid, * FROM quotes")
        return cursor.fetchall()

    def update(self, rowid, quote, name, year):
        '''
        Updates a row from the database with given values based on id
        :param quote: String
        :param name: String
        :param year: Integer
        :return: True
        :raises: Database errors on connection and insertion
        '''
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        params = {'rowid': rowid, 'quote': quote, 'name': name, 'year': year}
        cursor.execute(
            f'''UPDATE quotes
              SET quote = :quote, name = :name, year = :year
              WHERE rowid = :rowid
            ''',
            params
        )
        connection.commit()
        cursor.close()
        return True
    
    def delete(self, rowid):
        '''
        Deletes a row from the database based on given id
        :param id Integer
        :return: True
        :raises: Database errors on connection and deletion
        '''
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute(
            '''DELETE FROM quotes
                WHERE rowid = {}'''
            , rowid
        )
        connection.commit()
        cursor.close()
        return True
