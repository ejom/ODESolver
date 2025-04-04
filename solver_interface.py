import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from symbolic_solvers import solve_first_order_linear, solve_constant_coeff_homogeneous
from numeric_solvers import numeric_solve_single_ode
from system_solver import solve_input_system
import re

def preprocess_ode_input(ode_str):
    ode_str = re.sub(r"y''", "Derivative(y(x), x, 2)", ode_str)
    ode_str = re.sub(r"y'", "Derivative(y(x), x)", ode_str)
    ode_str = re.sub(r"(?<!\w)y(?!\()", "y(x)", ode_str)  # replace 'y' with 'y(x)' if not already a function
    return ode_str

def auto_detect_and_solve(ode_input):
    x = sp.symbols('x')
    y = sp.Function('y')
    try:
        ode_input = preprocess_ode_input(ode_input)

        if '=' in ode_input:
            lhs_str, rhs_str = ode_input.split('=', 1)
        else:
            lhs_str, rhs_str = ode_input, '0'

        lhs = sp.sympify(lhs_str.strip())
        rhs = sp.sympify(rhs_str.strip())
        full_eq = sp.Eq(lhs, rhs)

        ics = input("Enter initial conditions (e.g. y(0)=1, y'(0)=0), or leave blank: ").strip()
        ics_dict = {}
        if ics:
            for ic in ics.split(','):
                if '=' not in ic:
                    continue
                var, val = ic.split('=')
                var_sym = sp.sympify(preprocess_ode_input(var.strip()))
                val_num = sp.sympify(val.strip())
                ics_dict[var_sym] = val_num

        try:
            sol = sp.dsolve(full_eq, y(x), ics=ics_dict if ics_dict else None)
            print("Solution:", sol)

            ysol = sol.rhs
            if not ysol.has(sp.Symbol('C1')):
                f = sp.lambdify(x, ysol, 'numpy')
                x_vals = np.linspace(0, 10, 300)
                y_vals = f(x_vals)
                plt.plot(x_vals, y_vals)
                plt.title("Symbolic ODE Solution")
                plt.xlabel("x")
                plt.ylabel("y")
                plt.grid(True)
                plt.show()
            else:
                print("Note: General solution contains arbitrary constant.")

        except NotImplementedError:
            print("Falling back to numeric solver...")
            if y(x) in lhs.free_symbols and lhs.has(sp.Derivative(y(x), x)):
                ode_rhs = rhs
                y0_val = list(ics_dict.values())[0] if ics_dict else 1.0
                t, y_vals = numeric_solve_single_ode(ode_rhs, y0_val)
                plt.plot(t, y_vals)
                plt.title("Numeric ODE Solution")
                plt.xlabel("x")
                plt.ylabel("y")
                plt.grid(True)
                plt.show()

    except Exception as e:
        print("Could not parse or solve equation:", e)
