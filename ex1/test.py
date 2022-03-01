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
        with self.assertRaises(TypeError):
            self.assertRaises(TypeError, ex1.safe_call(ex1.f1,2.5,3.5))
            self.assertRaises(TypeError, ex1.safe_call(ex1.f1,"hell",3))
            self.assertRaises(TypeError, ex1.safe_call(ex1.f1,'s',3))
            self.assertRaises(TypeError, ex1.safe_call(ex1.f2, -2, "good luck"))
            self.assertRaises(TypeError, ex1.safe_call(ex1.f2, 230, 2))
            self.assertRaises(TypeError, ex1.safe_call(ex1.f2, 230, -59))
            self.assertRaises(TypeError, ex1.safe_call(ex1.f3, 45, -2))
            self.assertRaises(TypeError, ex1.safe_call(ex1.f3, 77.12, -23))
            self.assertRaises(TypeError, ex1.safe_call(ex1.f3, 77/25, (36*2)))

    """ testing !- testing Q2"""    
    def test_1(self):
        a = {"a":1,"c":3,"b":"2"}
        b = ((1,3,4,51,2))
        c = [24.2 ,"2","1","0"]
        d = {"d":[1,2],"b":"3","a":1}
        e = ("A","b","C","W")
        f = [10,12,11,9," ","te","st"]
        print(ex1.print_sorted(a)) 
        print(ex1.print_sorted(b))
        print(ex1.print_sorted(c))
        print(ex1.print_sorted(d))
        print(ex1.print_sorted(e))
        print(ex1.print_sorted(f))


    """ testing !- testing Q3"""
    def test_1(self):
        ex1.
if __name__ == '__main__':
    unittest.main()