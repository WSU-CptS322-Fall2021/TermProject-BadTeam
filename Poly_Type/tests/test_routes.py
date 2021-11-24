import unittest
import sys
#from app.Controller.hostRoutes import createCode
from app.Controller.hostRoutes import createCode
class TestRoutes(unittest.TestCase):

    def test_createcode(self):
        code = createCode()
        self.assertTrue(len(code) == 6)
        for i in range(0, 5):
            self.assertTrue(code[i] in 'ABCDEFGHJKLMNPQRSTUVWXYZ1234567890')
