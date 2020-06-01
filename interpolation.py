import sympy
import math
import numpy as np


def l_i(x, i, x_s):
    res = 1
    for j in range(len(x_s)):
        if j != i:
            res *= (x-x_s[j])/(x_s[i] - x_s[j])
    return res


def lagrange_polynomial(X, Y):
    L = 0
    x = sympy.symbols('x')
    for i in range(len(Y)):
        L += Y[i] * l_i(x, i, X)
    return sympy.expand(L)


def newton_polynomial(X, Y):
    x = sympy.symbols('x')
    g = Y[:]
    s = g[0]
    for i in range(len(Y)-1):
        g = [(g[j+1]-g[j])/(X[j+i+1]-X[j]) for j in range(len(g)-1)]
        s += g[0] * product(x-X[j] for j in range(i+1))
    return sympy.expand(s)

def new_newton_polynomial(X, Y):
    x = sympy.symbols('x')
    n = len(X)
    s = f(0, n - 1, X, Y)

    for i in range(n - 1):
        s *= (x - X[n - 2 - i])
        s += f(0, n - 2 - i, X, Y)
    return sympy.expand(s)

def f(i, j, X, Y):
    if j == i:
        return Y[j]
    a = f(i + 1, j, X, Y)
    b = f(i, j - 1, X, Y)
    return (a - b) / (X[j] - X[i])



def product(a):
    p = 1
    for i in a:
        p *= i
    return p


def chebyshev_nodes(a, b, n: int):
    x_nodes = list()
    for k in range(int(n)):
        k += 1
        x_nodes.append(math.cos((2*k - 1) / (2 * n) * math.pi))
    for i in range(n):
        x_nodes[i] = x_nodes[i] * 0.5 * (b - a) + 1/2 * (a + b)
    return x_nodes
