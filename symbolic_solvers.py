import sympy as sp

def solve_first_order_linear(a, b, c):
    x = sp.symbols('x')
    y = sp.Function('y')
    ode = sp.Eq(a(x)*sp.Derivative(y(x), x) + b(x)*y(x), c(x))
    sol = sp.dsolve(ode, y(x))
    return sol

def solve_constant_coeff_homogeneous(coeffs):
    x = sp.symbols('x')
    y = sp.Function('y')
    derivatives = [y(x).diff(x, i) for i in reversed(range(len(coeffs)))]
    lhs = sum(c*d for c, d in zip(coeffs, derivatives))
    ode = sp.Eq(lhs, 0)
    sol = sp.dsolve(ode, y(x))
    return sol
