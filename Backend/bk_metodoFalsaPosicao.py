from __future__ import division
from math import *
import numpy as np

def MFPosicao(f, a, b, Erro, itMax):
  it = 0
  x = a
  Er = 1
  matrizResult = []
  matrizResult.append(['K', 'A', 'X', 'F(A)', 'F(X)', 'F(B)', 'Er'])
  while(Er >= Erro and  it < itMax):
    xold = x
    x = a - f(a)*(b-a)/(f(b)-f(a))
    Er = np.abs((x - xold)/x)
    matrizResult.append([str(it), str(float(round(a, 6))), str(float(round(b, 6))), str(float(round(f(a), 6))),
                         str(float(round(f(x), 6))), str(float(round(f(b), 6))), str(float(round(Er, 8)))])
    if (f(a)*f(x) < 0):
      b = x
    else:
      a = x
    it = it + 1
  return matrizResult, x