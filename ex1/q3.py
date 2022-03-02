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

