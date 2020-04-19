import unittest # Importing the unittest module
from credentials import User# Importing the contact class

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


if __name__ == '__main__':
    unittest.main()