import numpy as np
from SolvingMethods.EulerSolver import EulerSolver
from SolvingMethods.MidpointSolver import MidpointSolver
from SolvingMethods.RungeKutt4Solver import RungeKutt4Solver
from SolvingMethods.TaylorSolver import TaylorSolver

def f(x,t):
    return -2*x + np.exp(t)
def f1(x,t):
    return 4*x - np.exp(t)
def f2(x,t):
    return -8*x + 3 * np.exp(t)

if __name__ == '__main__':
    print('Program starts')
    print('Initializing data...')

    init, a, b, n = 1, 0, 1, 10
    solutions = []
    methods = [EulerSolver(f, chart_color='red'),
               MidpointSolver(f, chart_color='green'),
               RungeKutt4Solver(f, chart_color='yellow'),
               TaylorSolver([f, f1, f2], chart_color='blue')]

    print('Calculating data...')

    for method in methods:
        method.solve(init, a, b, n)
        method.draw_plot(True)
        method.draw_frame()
        method.draw_global_error()

    print('Initializing data...')

    init, a, b, n = 1, 0, 1, 40

    print('Calculating data...')

    for method in methods:
        method.solve(init, a, b, n)
        method.draw_plot(True)
        method.draw_frame()
        method.draw_global_error()

    print('Program Finished')