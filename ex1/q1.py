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
        raise TypeError
    for i in range(len(types)):
        if types[i] == "none":
            continue
        if parse_type_txt(str(type(variables[i]))) != types[i]:
            raise TypeError
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