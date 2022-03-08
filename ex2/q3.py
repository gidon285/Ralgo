def _offset(func):
    def offset(self, *args): 
        if len(args) == 0:
            return func(self)
        if isinstance(args[0], int):
            return func(self,(self.lst,args[0]))
        else:
            _arguments = list(args[0])
            _temp_lst = self.lst
            for i in range(0,len(_arguments)):
                if i == len(_arguments) - 1:
                    return func(self,(_temp_lst,_arguments[i]))
                _temp_lst = _temp_lst[_arguments[i]]
    return offset

class List(list):
    def __init__(self, *args):
        if not isinstance(args[0], list):
            raise SyntaxError("List must be of type lists, got "+type(args[0])+" instead" )
        self.lst = list(args[0])    

    @_offset
    def __len__(self, *args):
        if len(args) != 0:
            ans, index = arg[0]
            return len(ans[index])
        else: 
            return self.lst.__len__()

    @_offset
    def __getitem__(self, *args):
        ans, index = args[0]
        return ans[index]

    @_offset
    def __delitem__(self, *args):
        ans, index = args[0]
        ans.__delitem__(index)
    
    def insert(self, i, val):
        self.lst.insert(i, val)

    def __setitem__(self, i, val):
        self.lst.__setitem__(i, val)

    def append(self, val):
        self.insert(len(self) + 1, val)
    
    def __str__(self):
        return self.lst.__str__()

arr1 = List([ [1,2] ])
arr2 = List([ [1,2], [2,1]])
arr3 = List([ [1,2], [2,1], [3,4] ])
arr4 = List([ [ [1,2], [3,4] ] ])
arr5 = List([ [ [ [1,2], [3,4] ] ] ])
arr6 = List([
    [[1,2,3,33],[4,5,6,66]],
    [[7,8,9,99],[10,11,12,122]],
    [[13,14,15,155],[16,17,18,188]]
])
