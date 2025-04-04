from solver_interface import auto_detect_and_solve
from system_solver import solve_input_system


def main():
    print("ODE Solver CLI")
    print("Choose mode:")
    print("1. Enter a differential equation")
    print("2. Solve a system of ODEs (dy/dt = Ay)")

    mode = input("Enter choice (1 or 2): ")
    if mode == '1':
        ode_input = input("Enter a differential equation (e.g. y'' + 3*y' + 2*y = 0): ")
        auto_detect_and_solve(ode_input)
    elif mode == '2':
        solve_input_system()
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
