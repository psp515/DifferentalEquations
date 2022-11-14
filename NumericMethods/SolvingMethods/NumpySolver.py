import types
from inspect import getfullargspec

import numpy as np
from scipy.integrate import odeint

from Interfaces.ISolvable import ISolvable
from Utils.InvalidArgumentInstanceException import InvalidArgumentInstanceException
from Utils.Solution import Solution
from Utils.UnimplementedException import UnimplementedException


class NumpySolver(ISolvable):
    def __init__(self, functions, name, chart_color='black'):
        super().__init__(functions, name, chart_color)

        if not isinstance(functions, types.FunctionType):
            raise InvalidArgumentInstanceException("Functions should be single function.")

        inspection = getfullargspec(functions)

        if len(inspection[0]) != 2:
            raise InvalidArgumentInstanceException("Functions should be function having 2 parameters.")

    def _method(self, i, results, linspace):
        raise UnimplementedException("Method is not implemented.")

    def solve(self, x0, a, b, n):
        linspace = np.linspace(a, b, n)
        return Solution(linspace, odeint(self.functions, x0, linspace), self.name, self.chart_color)