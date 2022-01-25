from math import *
from sympy import Symbol

x = Symbol('x')
def valAendB_log (f):
    a = 0.1
    b = 0.1
    i = 0
    while i <= 10:
        a = b
        b = b + 0.1
        if f(a) > 0 and f(b) < 0:
            return round(a, 2), round(b, 2)
        elif f(b) < 0 and f(a) > 0:
            return round(a, 2), round(b, 2)
        elif (f(a) < 0 and f(b) < 0) or (f(a) > 0 and f(b) > 0):
            a = b
            b += 0.1
        else:
            return round(a, 2), round(b, 2)
        i+=0.1

def valAendB_expre(f):
    a = 0
    b = 0
    k = -10
    while k <= 10:
        a = k
        b = k + 0.1
        if f(a) > 0 and f(b) < 0:              
            return (a, b)
        elif f(b) < 0 and f(a) > 0:
            return (a, b)          
        elif (f(a) < 0 and f(b) < 0) or (f(a) > 0 and f(b) > 0):  
            a = b
            b += 0.1
        else:             
            return (a,b)
        k += 0.1