"======================================================================="
"=========================      Q one with tests     ==================="
def f1(x:int, y):
    return x+y
def f2(x, y:float):
    return x+y
def f3(x:str, y:str):
    return x+y
def f4(x, y):
    return x+y
def safe_call(*args):
    """" safe_call makes sure that the given variables to a fucntions f are correct. if f dosent specify the type 
        of a given variable it wont be checked. first we parse the variables, then we convert the names to lists so we
        can accsess them via index. afterwards we check each variable if he has an annotation, the ones that do will be checked
        by comparing the types by parsing them into strings and checking compatabillity."""
    f , variables = f_out_args(args)
    f_given = parse_annons(f)
    types = prepare_arr(f_given)
    if len(variables) < len(types):
        raise TypeError("type error")
    for i in range(len(types)):
        if types[i] == "none":
            continue
        if parse_type_txt(str(type(variables[i]))) != types[i]:
            raise TypeError("type error")
    return f(*tuple(variables))
def prepare_arr(arr:list) -> list:
    """returns a list that has each variable type, and none if type isnt in annotations."""
    ans = []
    for var in arr['vars']:
        if var in arr:
            ans.append(arr[var])
        else:
            ans.append("none")
    return ans
def parse_annons(f) -> list:
    """ This method takes a function and extrackts its annotations and parse them into an dictionary, by name and value"""
    dictk = {}
    dictk["vars"] = f.__code__.co_varnames[:f.__code__.co_argcount]
    for anon in f.__annotations__:
        dictk[anon] =str(f.__annotations__[anon])[str(f.__annotations__[anon]).find("'")+1:str(f.__annotations__[anon]).rfind("'")]
    return dictk

def parse_type_txt(txt:str) -> str:
    """ side method, parses the text of the type into a single word."""
    return str(txt)[str(txt).find("'")+1:str(txt).rfind("'")]

def f_out_args(arguments):
    lst = []
    f = 0
    for arg in arguments:
        if "function" == parse_type_txt(str(type(arg))):
            f = arg
        else:
            lst.append(arg)
    return (f, lst)
  
def wins():
    """ tests for checking good input"""
    assert 5.5 == safe_call(f1,2,3.5) 
    assert 5 == safe_call(f1,2,3) 
    assert 1.5 == safe_call(f2, -2, 3.5)
    assert 3.5 == safe_call(f2, 2, 1.5)
    assert "hello world" == safe_call(f3, "hello", " world")
    assert "worldhello" == safe_call(f3, "world", "hello")
    assert "worldhello" == safe_call(f4, "world", "hello")
    x = 1 
    y = 8
    assert 9 == safe_call(f4, x, y)
    print("8 good inputs went ok.")

def fails():
    """ tests for checking bad input"""
    try:
        safe_call(f1,2.5,3.5)
        safe_call(f1,"hell",3)
        safe_call(f1,'s',3)
        safe_call(f2, -2, "good luck")
        safe_call(f2, 230, 2)
        safe_call(f2, 230, -59)
        safe_call(f3, 45, -2)
        safe_call(f3, 77.12, -23)
        safe_call(f3, 77/25, (36*2))
    except TypeError:
        pass
    print("8 bad inputs went ok. ")
# wins()
"======================================================================="
"=========================      Q two with tests     ==================="

def print_sorted(*args):
    for arg in args:
        print(req(arg))
def req(arg):
    if isinstance(arg, dict):
            #dict
            ans = sort_dict(arg)
            for val in ans:
                if has_type(arg[val]):
                    ans[val] = req(arg[val])
            return ans
    elif isinstance(arg, list):
            #list
            for i in range(len(arg)):
                arg[i] = req(arg[i])
            return msort(arg)
    elif isinstance(arg, tuple):
            #tuple
            lst = list(arg)
            for i in range(len(lst)):
                lst[i] = req(lst[i])
            ty = msort(lst)
            return tuple(ty)
    else:
        return arg

def msort(data) -> list:
    res =[]
    for txt in list(data):
        res.append(str(txt))
    res.sort()
    return res
def has_type(y):
    return isinstance(y, dict) or isinstance(y, list) or isinstance(y, tuple) or isinstance(y, set)

def sort_dict(myd):
    tempkeys = myd.keys()
    keys = []
    for k in tempkeys:
        keys.append(k)
    keys.sort()
    ans = {}
    for k in keys:
        ans[k] = myd[k]
    return ans

# x = {"a":5,"c":6,"b":[1,3,"2",2,4],"dic":{"a":1,"b":2},"tuple":(1,6,2,3,9)}
# t = ("c","a",[1,3,2,4],{"b":1,"a":2},(1,6,2,3,9))
# l = ["c","a",[1,3,2,4],{"b":1,"a":2},(1,6,2,3,9)]
# print_sorted(l)

"======================================================================="
"=========================      Q three with test    ==================="
epsilon = 0.005
def find_root(*args):
    """ using Newton's method to get the root of a funcion."""
    f , variables = f_out_args(args)
    a = abs(variables[0])
    for i in range(1,len(variables)):
        a = abs(a - abs(variables[i]))
    # a will be the absulot value (distance) between point a, and b( c, d , etc'...).
    x_0 = a
    x = a
    # 25 iterations returns a really good value in relation to the mthod.
    for i in range(25):
        f_org = f(x)
        f_tag = (( f(x+epsilon) - f(x) ) / epsilon);
        x_0 = x - (f_org / f_tag) 
        x = x_0
    return x_0

find_root(lambda x: x**2-2,1,4)