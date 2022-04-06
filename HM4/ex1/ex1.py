
import unittest

def bounded_subset(lst: list, num: int):
    if not isinstance(lst, list) or not isinstance(num, int):
        raise ValueError("This generator accepts only (list, int) input")
    temp = [ x for x in lst if x <= num].sort()
    ans = []
    for i in range(len(lst)):
        if i == 0 :
            ans.append([])
        ans.extend(subs for subs in [subset + [i] for subset in ans] if sum(subs) <= num)
    return ans

