from copy import copy
from glob import glob


a = 0
def sums(arg=None):
    global a

    if arg is None:
        print(a)
        b = copy(a)
        a = 0
        return b
    
    a += arg
    return sums

sums(5)() + 5 # 5
sums(5)(2)() # 7
sums(5)(100)(-10)() # 95
