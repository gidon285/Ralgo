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
def f(x):
    return x**2

print(f(3))
print(f(3))
print(f(2))
print(f(2))

