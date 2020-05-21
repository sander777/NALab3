import interpolation
import sympy as sp
import numpy as np
from math import *
import matplotlib.pyplot as plt

def f(x):
    return sin(4 * x)

#TODO: переробити Ньютона

a = 0
b = 2

n = int(input("Введіть степінь полінома n: "))
n += 1
step = (b - a)/n
plot_step = .001

X1 = list()
Y1 = list()

XC = list()
YC = list()

for i in np.arange(a, b, step):
    X1.append(i)
    Y1.append(f(i))

XC = interpolation.chebyshev_nodes(a, b, n)
YC = list(map(f, XC))

L = interpolation.lagrange_polynomial(X1, Y1)
L_func = sp.lambdify(sp.symbols('x'), L)

L_c= interpolation.lagrange_polynomial(XC, YC)
L_c_func = sp.lambdify(sp.symbols('x'), L_c)

N = interpolation.newton_polynomial(X1, Y1)
N_func = sp.lambdify(sp.symbols('x'), N)

N_c = interpolation.newton_polynomial(XC, YC)
N_c_func = sp.lambdify(sp.symbols('x'), N)


Xs = list(np.arange(a, b, plot_step))

Y_f = list(map(f, Xs))

Y_L = list(map(L_func, Xs))
Y_L_c = list(map(L_c_func, Xs))

Y_N = list(map(N_func, Xs))
Y_N_c = list(map(N_c_func, Xs))

plt.style.use('dark_background')

plt.subplot(3, 2, 1)
plt.plot(Xs, Y_f, color='#00ffff', linewidth="3", dash_capstyle='round')
plt.xlabel("x")
plt.ylabel("f(x)")

plt.subplot(3, 2, 2)
plt.plot(Xs, Y_L, color='#aa00ff', linestyle=":", linewidth="3", dash_capstyle='round')
plt.xlabel("x")
plt.ylabel("L(x)")

plt.subplot(3, 2, 3)
plt.plot(Xs, Y_L_c, color='#bb00ee', linestyle=":", linewidth="3", dash_capstyle='round')
plt.xlabel("x")
plt.ylabel("L_c(x)")

plt.subplot(3, 2, 4)
plt.plot(Xs, Y_N, color='#cc00dd', linestyle=":", linewidth="3", dash_capstyle='round')
plt.xlabel("x")
plt.ylabel("N(x)")

plt.subplot(3, 2, 5)
plt.plot(Xs, Y_N_c, color='#dd00cc', linestyle=":", linewidth="3", dash_capstyle='round')
plt.xlabel("x")
plt.ylabel("N_c(x)")

plt.show()