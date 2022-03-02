import unittest
import math
import q1 as q1
class TestStringMethods(unittest.TestCase):
    """ testing !- testing Q1"""
    def test_good(self):
        """ this is for good inputs"""
        self.assertEqual(5.5, q1.safe_call(q1.f1,2,3.5))
        self.assertEqual(5, q1.safe_call(q1.f1,2,3))
        self.assertEqual(1.5, q1.safe_call(q1.f2, -2, 3.5))
        self.assertEqual(3.5, q1.safe_call(q1.f2, 2, 1.5))
        self.assertEqual("hello world", q1.safe_call(q1.f3, "hello", " world") )
        self.assertEqual("world", q1.safe_call(q1.f4, "", "world"))
        self.assertEqual("worldhello", q1.safe_call(q1.f4, "world", "hello"))
        x = 1 
        y = 8
        self.assertEqual(9, q1.safe_call(q1.f4, x, y))
    def test_bad(self):
        """ this is for bad inputs"""
        with self.assertRaises(TypeError):
            self.assertRaises(TypeError, q1.safe_call(q1.f1,2.5,3.5))
            self.assertRaises(TypeError, q1.safe_call(q1.f1,"hell",3))
            self.assertRaises(TypeError, q1.safe_call(q1.f1,'s',3))
            self.assertRaises(TypeError, q1.safe_call(q1.f2, -2, "good luck"))
            self.assertRaises(TypeError, q1.safe_call(q1.f2, 230, 2))
            self.assertRaises(TypeError, q1.safe_call(q1.f2, 230, -59))
            self.assertRaises(TypeError, q1.safe_call(q1.f3, 45, -2))
            self.assertRaises(TypeError, q1.safe_call(q1.f3, 77.12, -23))
            self.assertRaises(TypeError, q1.safe_call(q1.f3, 77/25, (36*2)))
if __name__ == '__main__':
    unittest.main()