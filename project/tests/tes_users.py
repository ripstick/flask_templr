# project/tests/test_users.py

import unittest
from project import app

class ProjectTests(unittest.TestCase):
    ##################################
    ####### SETUP and Teardown #######
    ##################################

    #executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

        self.assertEquals(app.debug, False)

    # execute after each test
    def tearDown(self):
        pass

    ##################################
    ######### tests ##################
    ##################################

    def test_login_page(self):
        response = self.app.get('/login', follow_redirects=True)
        self.assertIn(b'Future site for logging into this app!', response.data)

if __name__ == "__main__":
    unittest.main()