from scipy.integrate import odeint

from Interfaces.ISolver import ISolver
from Utils.Solution import Solution

import numpy as np

class OdeintSolver(ISolver):
    def __init__(self, functions, name='Optimal', chart_color='black'):
        super().__init__(functions, name, chart_color)

    def solve(self, x0, a, b, n):
        linspace = np.linspace(a, b, n)
        sol = odeint(self.functions, x0, linspace)
        # array is simplyfied here
        return Solution(linspace, [x[0] for x in sol], self.name, self.chart_color)

    def _get_optimal(self, x0, a, b, n):
        return self.solve(x0, a, b, n)