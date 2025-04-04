import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

def numeric_solve_single_ode(ode_expr, y0_val, x0_val=0.0, xmax=10.0):
    x = sp.symbols('x')
    y = sp.Function('y')
    dydx = y(x).diff(x)
    ode_eq = sp.Eq(dydx, ode_expr)
    f_rhs = sp.lambdify((x, y(x)), ode_expr, 'numpy')

    def f(t, yval):
        return f_rhs(t, yval)

    sol = solve_ivp(f, (x0_val, xmax), [y0_val], t_eval=np.linspace(x0_val, xmax, 300))
    return sol.t, sol.y[0]
