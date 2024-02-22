class BaseModel:

    def create(self, quote, name, year):
        '''
        Creates new entry and inserts into database.
        :param quote: String
        :param name: String
        :param year: Integer
        :return: None
        :raises: Database errors on connection and insertion
        '''
        pass

    def read():
        '''
        Gets all entries from database
        :return: List of list containing all rows of database
        '''
        pass

    def update(self, id, quote, name, year):
        '''
        Updates entry in database
        :param id: UUID
        :param quote: String
        :param name: String
        :param year: Integer
        :return: None
        :raises: Database errors on connection and insertion
        '''
        pass
    
    def delete(self, id):
        """
        Deletes entry from database
        :param id: UUID
        :return: None
        :raises: Database errors on connection and deletion
        """
        pass


