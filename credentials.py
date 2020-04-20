class User:
    """
    Class that generates new instances of credentails.
    """

    users_list = [] # Empty list that will hold users details

    def __init__(self, first_name, last_name, password):


        self.first_name = first_name
        self.last_name = last_name
        self.password = password

       # Init method up here
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.users_list.append(self)

    @classmethod
    def confirm_user(cls, first_name, password):
        '''
        Method that confirm if the name and password entered are correct
        '''
        initial_user=""
        for user in User.users_list:
            if (user.first_name == user.first_name and user.password == password):
                initial_user = user.first_name
        return initial_user