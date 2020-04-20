import unittest # Importing the unittest module
from credentials import User, Credentials# Importing the contact class

class TestUssers(unittest.TestCase):

    '''
    Test class that defines test cases for the Credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''


    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Samwel","Rangili","Sam0758597216") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Samwel")
        self.assertEqual(self.new_user.last_name,"Rangili")
        self.assertEqual(self.new_user.password,"Sam0758597216")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the users list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.users_list), 3)


    def test_confirm_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user = User("Samwel", "Rangili", "Sam0758597216")
            self.new_user.save_user()
            user2 = User("Annitter", "Mitchelle", "xyz3980168")
            user2.save_user()

            for user in User.users_list:
                if user.first_name == user2.first_name and user.password == user2.password:
                    initial_user = user.first_name
                    return initial_user

            self.assertEqual(initial_user, User.confirm_user(user2.password, user2.first_name))

            # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the Credentials class behaviours.

    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credentials("Samwel", "Facebook", "SamwelRangili", "Sam3980168") # create credential object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.user_name,"Samwel")
        self.assertEqual(self.new_credential.site_name,"Facebook")
        self.assertEqual(self.new_credential.account_name,"SamwelRangili")
        self.assertEqual(self.new_credential.password, "Sam3980168")

    def test_save_credentials(self):
        '''
        Test case to check if we can save credentials to the credentials list.
        '''
        self.new_credential.save_credential()
        Email = Credentials("Festus", "Email", "festusayosi", "Ayosi254")
        Email.save_credential()
        self.assertEqual(len(Credentials.credentials_list), 2)

if __name__ == '__main__':
    unittest.main()