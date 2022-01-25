from __future__ import division  
from math import *

def bissecao(f, a, b, TOL):
    fa = f(a)
    Er = 1
    matrizResult = []
    matrizResult.append(['K', 'A', 'B', 'X0', 'F(A)', 'F(B)', 'F(X0)', 'Er'])
    #cont = (log10(b - a) - pow(log10(10), -2)) / log10(2)
    #N = abs(round(cont, 0))
    i = 1
    while Er > TOL:
        p = a + (b-a)/2  
        fp = f(p)  
        Er = (b-a)/2
        matrizResult.append([str(i), str(float(round(a, 6))), str(float(round(b, 6))), str(float(round(p, 6))), str(float(round(f(a), 6))), str(float(round(f(b), 6))), str(float(round(f(p), 6))), str(float(round(Er, 6)))])
        if ((fp == 0) or ((b-a)/2 < TOL)):
            return (matrizResult, p, i)
        if (float(fa) * float(fp) > 0):
            a = p  
            fa = fp  
        else:  
            b = p
        i += 1
    raise NameError("Num. max. de iter. excedido!");
