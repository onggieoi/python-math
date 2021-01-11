from scipy import optimize
from math import exp
from scipy import integrate
import numpy as np

# -------------------------

# f(x) = (x**2 -2x)exp(3-x)


def f(x):
    return x*(x - 2)*exp(3 - x)


def fp(x):
    return -(x**2 - 4*x + 2)*exp(3 - x)


optimize.newton(f, 1, fprime=fp)  # Using the Newton-Raphson method 2.0

# Using x1 = 1.5 and the secant method # 1.9999999999999862
optimize.newton(f, 1., x1=1.5)


# --------------------------
def erf_integrand(t):
    return np.exp(-t**2)


val_quad, err_quad = integrate.quad(erf_integrand, -1.0, 1.0)
# (1.493648265624854, 1.6582826951881447e-14)

val_quadr, err_quadr = integrate.quadrature(erf_integrand, -1.0, 1.0)
# (1.4936482656450039, 7.459897144457273e-10)
