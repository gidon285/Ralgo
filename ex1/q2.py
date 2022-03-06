def print_sorted(*args):
    for arg in args:
        print(req(arg))
    return args
def req(arg):
    if isinstance(arg, dict):
            #dict
            ans = sort_dict(arg)
            for val in ans:
                ans[val] = req(arg[val])
            return ans
    elif isinstance(arg, list):
            #list
            for i in range(len(arg)):
                arg[i] = req(arg[i])
            return sorted(arg, key=str)
    elif isinstance(arg, tuple):
            #tuple
            lst = list(arg)
            for i in range(len(lst)):
                lst[i] = req(lst[i])
            ty = sorted(arg, key=str)
            return tuple(ty)
    else:
        return arg

def has_type(y):
    return isinstance(y, dict) or isinstance(y, list) or isinstance(y, tuple) or isinstance(y, set)

def sort_dict(myd):
    return {k:myd[k] for k in sorted(myd.keys())}

