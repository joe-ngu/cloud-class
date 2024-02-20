from abc import ABC, abstractmethod

class BaseModel(ABC):

    @abstractmethod
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

    @abstractmethod
    def read():
        '''
        Gets all entries from database
        :return: List of list containing all rows of database
        '''
        pass

    @abstractmethod
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
    
    @abstractmethod
    def delete(self, id):
        """
        Deletes entry from database
        :param id: UUID
        :return: None
        :raises: Database errors on connection and deletion
        """
        pass


