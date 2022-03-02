import unittest
import math
import q3 as q3
class TestStringMethods(unittest.TestCase):
    """ testing !- testing Q3"""
    def test_1(self):
        self.assertEqual(1.414213562373095, q3.find_root(lambda x: x**2-2,1,4))
        self.assertEqual(1.5596104694623694, q3.find_root( lambda x: (math.pow(x, x) - 2),0,5))

if __name__ == '__main__':
    unittest.main()