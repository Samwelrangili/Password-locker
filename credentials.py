import string
import pyperclip
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

class Credentials:
    '''
    Class that generates instances of account credentials, and save information
    '''

    credentials_list = []
    users_credentials_list = []

    def __init__(self, user_name, site_name, account_name, password):
        '''
        __init__ method that define properties of inserted objects
        '''

        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password

    def save_credential(self):
        '''
        method that save credentials in the credential_list
        '''
        Credentials.credentials_list.append(self) 

    @classmethod
    def display_credential(cls, user_name):
        '''
        Class method to show the list of credentials saved
        '''
        users_credentials_list = []
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                users_credentials_list.append(credential)
        return users_credentials_list 

    @classmethod
    def findby_site_name(cls, site_name):
        '''
        method that validate site name.
        '''
        for credential in cls.credentials_list:
            if credential.site_name == site_name:
                return credential 

                
    @classmethod
    def credential_exist(cls, site_name):
        '''
        method that checks if a credential exists in credential_list.
        '''
        for credential in cls.credentials_list:
            if credential.site_name == site_name:
                return True
        return False 

    @classmethod
    def copy_credential(cls, site_name):
        '''
        Class method that copies a credentials details after the credentials site_name has been entered
        '''
        find_credential = Credentials.findby_site_name(site_name)
        return pyperclip.copy(find_credential.password)

    def delete_credential(self):
        '''
        Method that deletes saved credential from credential_list
        '''
        Credentials.credentials_list.remove(self)