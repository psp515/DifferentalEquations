from scipy.integrate import odeint

from Interfaces.ISolver import ISolver
from Utils.Solution import Solution

import numpy as np

class NumpySolver(ISolver):
    def __init__(self, functions, name='Optimal', chart_color='black'):
        super().__init__(functions, name, chart_color)

    def solve(self, x0, a, b, n):
        linspace = np.linspace(a, b, n)
        return Solution(linspace, odeint(self.functions, x0, linspace), self.name, self.chart_color)

    def draw_plot(self, x0, a, b, n, draw_optimal_solution=False):
        super().draw_plot(x0, a, b, n, False)

    def _get_optimal(self, x0, a, b, n):
        return self.solve(x0, a, b, n)