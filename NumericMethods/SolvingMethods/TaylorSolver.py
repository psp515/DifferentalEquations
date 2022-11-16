from inspect import getfullargspec
from Interfaces.ISolver import ISolver
from Utils.InvalidArgumentInstanceException import InvalidArgumentInstanceException


class TaylorSolver(ISolver):
    def __init__(self, functions, name='Taylor', chart_color='black'):

        if not type(functions) == list:
            raise InvalidArgumentInstanceException("Functions should be list of functions.")

        if len(functions) == 0:
            raise InvalidArgumentInstanceException("Functions should contain at least one function.")

        for f in functions:
            inspection = getfullargspec(f)
            if len(inspection[0]) != 2:
                raise InvalidArgumentInstanceException("Each function should have 2 parameters.")

        if not isinstance(chart_color, str):
            raise InvalidArgumentInstanceException("Chart color should be string.")

        self.chart_color = chart_color
        self.functions = functions
        self.name = name
        self._solution = None
        self._optimal_solution = None

    def _method(self, i, results, linspace):
        diff = linspace[i+1] - linspace[i]
        f_count = len(self.functions)
        result = results[i]
        x, t = results[i], linspace[i]
        sil = 1
        for j in range(f_count):
            sil = sil / (j + 1)
            k = self.functions[j](x, t)
            result += sil * k * (diff**(j+1))

        return result