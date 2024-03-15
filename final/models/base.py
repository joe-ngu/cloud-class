class FoodsBaseModel:
    '''
    Base class for food model
    '''
    def create(self, name, quantity):
        '''
        Creates new food item and inserts into database.
        :param name: String
        :param quantity: Float
        :return: None
        '''
        pass

    def read():
        '''
        Gets all food items from meal
        :return: List of list containing all food items
        '''
        pass

    def update(self, name, quantity):
        '''
        Updates food item in database
        :param name: String
        :param quantity: Float
        :return: None
        '''
        pass
    
    def delete(self, id):
        """
        Deletes food item from database
        :param id: UUID
        :return: None
        """
        pass