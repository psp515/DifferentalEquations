import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

from SolvingMethods.EulerSolver import EulerSolver
from SolvingMethods.MidpointSolver import MidpointSolver
from SolvingMethods.NumpySolver import NumpySolver
from SolvingMethods.RungeKutt4Solver import RungeKutt4Solver
from SolvingMethods.TaylorSolver import TaylorSolver


def f(x, t):
    return -3*x+2*np.exp(-t)

def f1(x, t):
    return x-1/t**2

def f12(x, t):
    return -(1/t)

def make_plot(solutions):
    for sol in solutions:
        plt.plot(sol.space, sol.results, sol.chart_color, label=rf'${sol.name}$')

    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    print('Program starts')
    print('Initializing data...')
    init, a, b, n = 2, 0, 1, 11
    solutions = []
    methods = [NumpySolver(f, chart_color='black'),
               EulerSolver(f, chart_color='red'),
               MidpointSolver(f, chart_color='green'),
               RungeKutt4Solver(f, chart_color='yellow'),]
               #TaylorSolver([f, f12], chart_color='blue')]
    print('Calculating data...')


    print(EulerSolver(f, chart_color='red').draw_frame(init,a,b,n))

    for method in methods:
        solutions.append(method.solve(init, a, b, n))
    print('Creating graph...')
    make_plot(solutions)
    print('Program Finished')