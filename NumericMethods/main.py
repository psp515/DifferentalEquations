import numpy as np

from SolvingMethods.EulerSolver import EulerSolver
from SolvingMethods.MidpointSolver import MidpointSolver
from SolvingMethods.RungeKutt4Solver import RungeKutt4Solver
from SolvingMethods.TaylorSolver import TaylorSolver


def f(x, t):
    return -3*x+2*np.exp(-t)

def f1(x, t):
    return x-1/t**2

def f12(x, t):
    return -(1/t)

if __name__ == '__main__':
    print('Program starts')
    print('Initializing data...')

    init, a, b, n = 2, 0, 1, 11
    solutions = []
    methods = [EulerSolver(f, chart_color='red'),
               MidpointSolver(f, chart_color='green'),
               RungeKutt4Solver(f, chart_color='yellow'),
               TaylorSolver([f], chart_color='blue')]

    print('Calculating data...')

    for method in methods:
        method.draw_plot(init, a, b, n, True)
        method.draw_frame(init, a, b, n)

    print('Program Finished')