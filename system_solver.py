import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def solve_system_homogeneous(A, y0, t_span):
    def system(t, y):
        return A @ y

    sol = solve_ivp(system, t_span, y0, t_eval=np.linspace(t_span[0], t_span[1], 300))
    return sol.t, sol.y

def solve_input_system():
    n = int(input("Enter the number of equations (dimension of the system): "))
    print("Enter coefficient matrix A row by row, separated by commas.")
    A = []
    for i in range(n):
        row = input(f"Row {i+1}: ")
        A.append([float(num) for num in row.strip().split(",")])
    A = np.array(A)

    y0 = [float(num) for num in input("Enter initial values (comma-separated): ").split(",")]
    t_span = tuple(map(float, input("Enter time span (start,end): ").split(",")))

    t, y = solve_system_homogeneous(A, y0, t_span)
    for i in range(y.shape[0]):
        plt.plot(t, y[i], label=f"y{i+1}(t)")
    plt.title("System of ODEs Solution")
    plt.xlabel("Time")
    plt.ylabel("Values")
    plt.legend()
    plt.grid(True)
    plt.show()
