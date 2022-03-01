import unittest
import ex1 as ex1
class TestStringMethods(unittest.TestCase):
    """ testing !- testing Q1"""
    def test_good(self):
        """ this is for good inputs"""
        self.assertEqual(5.5, ex1.safe_call(ex1.f1,2,3.5))
        self.assertEqual(5, ex1.safe_call(ex1.f1,2,3))
        self.assertEqual(1.5, ex1.safe_call(ex1.f2, -2, 3.5))
        self.assertEqual(3.5, ex1.safe_call(ex1.f2, 2, 1.5))
        self.assertEqual("hello world", ex1.safe_call(ex1.f3, "hello", " world") )
        self.assertEqual("world", ex1.safe_call(ex1.f4, "", "world"))
        self.assertEqual("worldhello", ex1.safe_call(ex1.f4, "world", "hello"))
        x = 1 
        y = 8
        self.assertEqual(9, ex1.safe_call(ex1.f4, x, y))
    def test_bad(self):
        """ this is for bad inputs"""
        self.assertRaises(TypeError, ex1.f2ex1.f2safe_call(ex1.f2f1,2.5,3.5))
        self.assertRaises(TypeError, ex1.f2safe_call(ex1.f2f1,"hell",3))
        self.assertRaises(TypeError, ex1.f2safe_call(ex1.f2f1,'s',3))
        self.assertRaises(TypeError, ex1.f2safe_call(ex1.f2f2, -2, "good luck"))
        self.assertRaises(TypeError, ex1.f2safe_call(ex1.f2f2, 230, 2))
        self.assertRaises(TypeError, ex1.f2safe_call(ex1.f2f2, 230, -59))
        self.assertRaises(TypeError, ex1.f2safe_call(ex1.f2f3, 45, -2))
        self.assertRaises(TypeError, ex1.f2safe_call(ex1.f2f3, 77.12, -23))
        self.assertRaises(TypeError, ex1.f2safe_call(ex1.f2f3, 77/25, (36*2)))

""" testing !- testing Q2"""

""" testing !- testing Q3"""

if __name__ == '__main__':
    unittest.main()