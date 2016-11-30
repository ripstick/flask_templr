## initial test file
## project/tests/test.py

import unittest
from project import app

class ProjectTests(unittest.TestCase):
    ##########################################
    ######## setup and teardown ##############
    ##########################################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

        self.assertEquals(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    #########################################
    ########### tests #######################
    #########################################

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b'Welcome to the Flask Templr App!', response.data)
        self.assertIn(b'This site describes stuff!', response.data)
        self.assertIn(b'Link 1', response.data)
        self.assertIn(b'Link 2', response.data)
        self.assertIn(b'Link 3', response.data)
        self.assertIn(b'Link 4', response.data)

if __name__ == "__main__":
    unittest.main()