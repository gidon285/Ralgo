flag = None
def lastcall(func1):
    def wrapper(*args, **kwargs):
        global flag
        var = args[0]
        if flag is None:
            flag = args[0]
            return "the answer is: " + str(func1(flag))
        elif flag == var:
            return "i already told you the answer, it was : " + str(func1(flag))
        else:
            flag = var
            return "the answer is: " + str(func1(flag)) 
    
    return wrapper
    
@lastcall
def f_int(x):
    return x**2
@lastcall
def f_str(x):
    return str(x) + " wow!"
@lastcall
def f_float(x):
    return x / 0.1
