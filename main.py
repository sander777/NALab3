import interpolation
import sympy as sp
import numpy as np
from math import *
import matplotlib.pyplot as plt

def f(x):
    return sin(4 * x)

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

N = interpolation.new_newton_polynomial(X1, Y1)
N_func = sp.lambdify(sp.symbols('x'), N)

N_c = interpolation.new_newton_polynomial(XC, YC)
N_c_func = sp.lambdify(sp.symbols('x'), N_c)


Xs = list(np.arange(a, b, plot_step))

Y_f = list(map(f, Xs))

Y_L = list(map(L_func, Xs))
Y_L_c = list(map(L_c_func, Xs))

Y_N = list(map(N_func, Xs))
Y_N_c = list(map(N_c_func, Xs))

plt.style.use('dark_background')

plt.subplot(2, 1, 1)
plt.plot(Xs, Y_f, color='#00ffff', linewidth="1", dash_capstyle='round')
plt.xlabel("x")

plt.plot(Xs, Y_L, color='#ff00ff', linestyle=":", linewidth="1", dash_capstyle='round')
plt.xlabel("x")

plt.plot(Xs, Y_N, color='#ffff00', linestyle=":", linewidth="1", dash_capstyle='round')
plt.xlabel("x")

plt.plot(X1, Y1, "ro", color='#ff0000')
plt.xlim(a, b)
plt.ylim(-3, 3)

plt.subplot(2, 1, 2)

plt.plot(Xs, Y_f, color='#00ffff', linewidth="1", dash_capstyle='round')
plt.xlabel("x")

plt.plot(Xs, Y_L_c, color='#ff00ff', linestyle=":", linewidth="1", dash_capstyle='round')
plt.xlabel("x")

plt.plot(Xs, Y_N_c, color='#ffff00', linestyle=":", linewidth="1", dash_capstyle='round')
plt.xlabel("x")

plt.plot(XC, YC, "ro", color='#ff0000')

plt.xlim(a, b)
plt.ylim(-3, 3)
plt.show()