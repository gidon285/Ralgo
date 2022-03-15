import unittest
import q2 as q2
class TestStringMethods(unittest.TestCase):
    """ testing !- testing Q1"""
    def test_good(self):
        """ this is for good inputs"""
        self.assertEqual(q2.f_int(2), "the answer is: " + str(4))
        self.assertEqual(q2.f_int(2), "i already told you the answer, it was : " + str(4))
        self.assertEqual(q2.f_int(3), "the answer is: " + str(9))
        self.assertEqual(q2.f_int(3), "i already told you the answer, it was : " + str(9))
        
        self.assertEqual(q2.f_str(2), "the answer is: " + str(2) + " wow!")
        self.assertEqual(q2.f_str(2), "i already told you the answer, it was : " + str(2) + " wow!")
        self.assertEqual(q2.f_str("gidon"), "the answer is: " + "gidon" + " wow!")
        self.assertEqual(q2.f_str("gidon"), "i already told you the answer, it was : " + "gidon" + " wow!")

        self.assertEqual(q2.f_float(0.1), "the answer is: " + str(1.0))
        self.assertEqual(q2.f_float(0.1), "i already told you the answer, it was : " + str(1.0))
        self.assertEqual(q2.f_float(0.2), "the answer is: " + str(2.0))
        self.assertEqual(q2.f_float(0.2), "i already told you the answer, it was : " + str(2.0))
    
    def test_bad(self):
        """ this is for bad inputs"""
        self.assertNotEqual(q2.f_int(2), "i already told you the answer, it was : " + str(4))
        self.assertNotEqual(q2.f_float(0.2), "i already told you the answer, it was : " + str(2.0))
        self.assertNotEqual(q2.f_str("gidon"), "i already told you the answer, it was : " + "gidon" + " wow!")

if __name__ == '__main__':
    unittest.main()