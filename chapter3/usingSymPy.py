import sympy
from sympy.utilities import lambdify

# f(x) = (x**2 -2x)e**(3-x)

x = sympy.symbols('x')

f = (x**2 - 2*x)*sympy.exp(3 - x)

# differentiate
fp = sympy.simplify(sympy.diff(f))  # (x*(2 - x) + 2*x - 2)*exp(3 - x)

# Check differentiate mually
fp2 = (2*x - 2)*sympy.exp(3 - x) - (x**2 - 2*x)*sympy.exp(3 - x)
sympy.simplify(fp2 - fp) == 0  # True

# integrate
F = sympy.integrate(f, x)  # -x**2*exp(3 - x)

# This converts a SymPy expression to a numerical expression that uses the NumPy
# equivalents of the SymPy standard functions to evaluate the expressions numerically
lam_f = lambdify(x, f)
lam_fp = lambdify(x, fp)
