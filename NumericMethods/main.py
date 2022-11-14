import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import odeint

from SolvingMethods.EulerSolver import EulerSolver
from SolvingMethods.MidpointSolver import MidpointSolver
from SolvingMethods.NumpySolver import NumpySolver


def f1(x, t):
    return -3*x+2*np.exp(-t)

def make_plot(solutions):
    for sol in solutions:
        plt.plot(sol.x, sol.results, sol.chart_color, label=rf'${sol.name}$')

    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    print('Program starts')
    init, a, b, n = 2, 0, 1, 11

    solutions = []
    methods = [NumpySolver(f1, "Optimal", 'black'),
               EulerSolver(f1, "Euler", 'red'),
               MidpointSolver(f1, "Midpoint", 'green'),
               MidpointSolver(f1, "Runge-Kutt", 'yellow')]

    for method in methods:
        solutions.append(method.solve(init, a, b, n))

    make_plot(solutions)