class Credentials:
    """
    Class that generates new instances of credentails.
    """

    user_list = [] # Empty list that will hold users details

    def __init__(self,first_name,last_name,password):


        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = password