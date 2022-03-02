import unittest
import math
import q2 as q2
class TestStringMethods(unittest.TestCase):
    """ testing !- testing Q1"""
    def test_1(self):
        a = {"a":1,"c":3,"b":"2"}
        b = ((1,3,4,51,2))
        c = [24.2 ,"2","1","0"]
        d = {"d":[1,2],"b":"3","a":1}
        e = ("A","b","C","W")
        f = [10,12,11,9," ","te","st"]
        print(q2.print_sorted(a)) 
        print(q2.print_sorted(b))
        print(q2.print_sorted(c))
        print(q2.print_sorted(d))
        print(q2.print_sorted(e))
        print(q2.print_sorted(f))
if __name__ == '__main__':
    unittest.main()