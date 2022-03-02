def print_sorted(*args):
    for arg in args:
        print(req(arg))
    return args
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