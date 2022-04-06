
import unittest

def bounded_subset(lst: list, n: int):
    if not isinstance(lst, list) or not isinstance(n, int):
        raise Exception("wrong input")
    temp = sorted([ x for x in lst if x <= n])
    ans = [[]]
    for num in lst:
        ans.extend(val for val in [a + [num] for a in ans] if sum(val) <= n)
    return ans

class tests(unittest.TestCase):

    def test_subsets(self):
        lst1 = [ 5, 2 ,6 ,10, 1]
        ans1 = bounded_subset(lst1, 10)
        self.assertTrue(ans1.__contains__([]))
        self.assertTrue(ans1.__contains__([2,6]))
        self.assertTrue(not ans1.__contains__([16]))


        lst2 = [ 5, 6 ,7 ,8, 9]
        ans2 = bounded_subset(lst1, 11)
        self.assertTrue(ans2.__contains__([]))
        self.assertTrue(ans2.__contains__([5,6]))
        self.assertTrue(not ans2.__contains__([16]))

    def test_bad_inputs(self):
        n = 5
        obj1= {"a":"1","b":"2"}
        obj2= {"c":"3","d":"4"}
        obj3= ({"a":"2","b":"3"})
        obj4= ("a","2","b","3")
        obj5= (10 ,9, 8, 7)
        try:
            check = bounded_subset(obj1, n)
        except Exception:
            pass
        try:
            check = bounded_subset(obj2, n)
        except Exception:
            pass
        try:
            check = bounded_subset(obj3, n)
        except Exception:
            pass
        try:
            check = bounded_subset(obj4, n)
        except Exception:
            pass
        try:
            check = bounded_subset(obj1, n)
        except Exception:
            pass
        try:
            check = bounded_subset(obj5, n)
        except Exception:
            self.assertEqual(True,True)

if __name__ == "__main__":
    unittest.main()
