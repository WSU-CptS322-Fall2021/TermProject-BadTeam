import unittest
import sys
#from app.Controller.hostRoutes import createCode
from app.Controller.hostRoutes import createCode, view_challenges
class TestRoutes(unittest.TestCase):

    def test_createcode(self):
        code = createCode()
        self.assertTrue(len(code) == 6)
        for i in range(0, 5):
            self.assertTrue(code[i] in 'ABCDEFGHJKLMNPQRSTUVWXYZ1234567890')
    def test_view_challenges(self):
        print("test")
        #tester = view_challenges(self)x
        #response = tester.get('/view_challenges')
        #self.assertTrue(response.status_code, 200)
