class FoodsBaseModel:
    '''Base class for food model'''
    def create(self, name, calories, fat, carbs, protein, quantity):
        '''
        Creates new food item and inserts into database.
        :param name: String
        :param calories: Float
        :param fat: Float
        :param carbs: Float
        :param protein: Float
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
    
    def delete(self):
        """
        Deletes all food item from database
        :return: None
        """
        pass