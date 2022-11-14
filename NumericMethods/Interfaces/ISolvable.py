from inspect import isclass

import numpy as np

from Utils.InvalidArgumentInstanceException import InvalidArgumentInstanceException
from Utils.Solution import Solution


class ISolvable:
    def __init__(self, functions, name, chart_color):
        self.functions = functions
        self.name = name

        if not isinstance(chart_color, str):
            raise InvalidArgumentInstanceException("Chart color should be string.")

        self.chart_color = chart_color

    def _method(self, i, results, linspace):
        return 0

    def solve(self, x0, a, b, n):
        linspace = np.linspace(a, b, n)
        results = np.zeros(n)
        results[0] = x0

        for i in range(n-1):
            results[i+1] = self._method(i, results, linspace)

        return Solution(linspace, results, self.name, self.chart_color)