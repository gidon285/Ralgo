import unittest
import q3 as q3

arr1 = q3.List([ [1,2] ])
arr2 = q3.List([ [1,2], [2,1]])
arr3 = q3.List([ [1,2], [2,1], [3,4] ])
arr4 = q3.List([ [ [1,2], [3,4] ] ])
arr5 = q3.List([ [ [ [1,2], [3,4] ] ] ])
arr6 = q3.List([
    [[1,2,3,33],[4,5,6,66]],
    [[7,8,9,99],[10,11,12,122]],
    [[13,14,15,155],[16,17,18,188]]
])
class TestStringMethods(unittest.TestCase):
    """ testing !- testing Q1"""
    def test_good(self):
        """ this is for good inputs"""
        self.assertEqual(arr1[0], [1,2])
        self.assertEqual(arr2[0], [1,2])
        self.assertEqual(arr3[0], [1,2])
        self.assertEqual(arr4[0], [[1,2],[3,4]])
        self.assertEqual(arr5[0], [[[1,2],[3,4]]] )
        self.assertEqual(arr5[0,0,1], [3,4])
        self.assertEqual(arr2[0,0], 1)

        self.assertEqual(len(arr2[0]), 2)
        self.assertEqual(len(arr5), 1)
        self.assertEqual(len(arr6), 3)
        self.assertEqual(len(arr6[1,0]), 4)
        
        self.assertEqual(str(arr1), "[[1, 2]]")
        self.assertEqual(str(arr2), "[[1, 2], [2, 1]]")
        self.assertEqual(str(arr3), "[[1, 2], [2, 1], [3, 4]]")

        arr1.append(0)
        self.assertEqual(str(arr1), "[[1, 2], 0]")
        del(arr1[1])
        self.assertEqual(str(arr1), "[[1, 2]]")

        arr2.append(0)
        self.assertEqual(str(arr2), "[[1, 2], [2, 1], 0]")
        del(arr2[2])
        self.assertEqual(str(arr2), "[[1, 2], [2, 1]]")


if __name__ == '__main__':
    unittest.main()



