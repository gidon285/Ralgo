def _offset(func):
    def offset(self, *args): 
        if len(args) == 0:
            return func(self)
        if isinstance(args[0], int):
            return func(self,args[0])
        else:
            _arguments = list(args[0])
            _temp_lst = self
            for i in range(0,len(_arguments)):
                if i == len(_arguments) - 1:
                    return func(_temp_lst,_arguments[i])
                _temp_lst = List(_temp_lst[_arguments[i]])
    return offset

class List(list):
    def __init__(self, *args):
        if not isinstance(args[0], list):
            raise SyntaxError("List must be of type lists, got "+type(args[0])+" instead" )
        super().__init__(*args)

    @_offset
    def __getitem__(self, *args):
        index = args[0]
        return super().__getitem__(index)

    @_offset
    def __delitem__(self, *args):
        index = args[0]
        return super().__delitem__(index)