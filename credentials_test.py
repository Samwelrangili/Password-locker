import unittest # Importing the unittest module
import pyperclip
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
        test_save method that check if we can we can save credentials in credential_list.
        '''
        self.new_credential.save_credential()
        Email = Credentials("Festus", "Email", "festusayosi", "Ayosi254")
        Email.save_credential()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_display_credentials(self):
        '''
        test_display method that check of our credentials are displying.
        '''
        self.new_credential.save_credential()
        Email = Credentials("Festus", "Email", "festusayosi", "ayosi254")
        Email.save_credential()
        LinkedIn = Credentials("Kevin", "LinkedIn", "KevinShorry", "shorry@254")
        LinkedIn.save_credential()
        self.assertEqual(len(Credentials.display_credential(Email.user_name)), 1)

    def tearDown(self):
        '''
        tearDown method that clears the users credentials list after each test case.
        '''
        Credentials.credentials_list = []

    def test_find_by_site_name(self):
        '''
        Test case to test if we can search credential by site_name and return the correct credential.
        '''
        self.new_credential.save_credential()
        LinkedIn = Credentials("Kevin","LinkedIn",'KevinShorry',"shorry@254")
        LinkedIn.save_credential()
        credential_exists = Credentials.find_by_site_name("LinkedIn")
        self.assertEqual(credential_exists, LinkedIn)

    def test_copy_credential(self):
        '''
        method to test if the copied credential is correct.
        '''
        self.new_credential.save_credential()
        Facebook = Credentials("Samwel","Facebook","SamwelRangili","Sam3980168")
        Facebook.save_credential()
        find_credential = None
        for credential in Credentials.users_credentials_list:
            find_credential = Credentials.findby_site_name(credential.site_name)
            return pyperclip.copy(find_credential.password)
        Credentials.copy_credential(self.new_credential.site_name)
        self.assertEqual("Sam3980168", pyperclip.paste())
        print(pyperclip.paste())

    def test_credential_exist(self):
        '''
        method that check if the credential exists in the credential_list.
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("Samwel","Facebook","SamwelRangili","Sam3980168")
        test_credential.save_credential()

        credential_exist = Credentials.credential_exist("Facebook")
        self.assertTrue(credential_exist)

    def test_delete_credential(self):
        '''
        method that test if we can delete saved credential from credential_list.
        '''
        self.new_credential.save_credential()
        new_credential = Credentials("Kevin","LinkedIn","KevinShorry","shorry@254")
        new_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credentials.credentials_list), 1)

    # def tearDown(self):
    #     '''
    #     tearDown method that clears the users credentials list after each test case.
    #     '''
    #     Credentials.credentials_list = []


if __name__ == '__main__':
    unittest.main()