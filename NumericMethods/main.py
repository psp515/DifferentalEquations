import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import odeint

from SolvingMethods.EulerSolver import EulerSolver


def f1(x, t):
    return -3*x+2*np.exp(-t)

if __name__ == '__main__':
    print('Program starts')
    init = 2
    t1 = np.linspace(0, 1, 11)
    sol_d1 = odeint(f1, init, t1)
    sol_d2 = EulerSolver(f1, "Euler").solve(init, 0, 1, 11)
    plt.plot(t1, sol_d1[:, 0], 'blue', label=r'$dokładne$')
    plt.plot(t1, sol_d2.results, 'red', label=rf'${sol_d2.method_name}$')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()