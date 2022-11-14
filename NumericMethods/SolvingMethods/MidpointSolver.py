import types
from inspect import  getfullargspec

from Interfaces.ISolvable import ISolvable
from Utils.InvalidArgumentInstanceException import InvalidArgumentInstanceException


class MidpointSolver(ISolvable):
    def __init__(self, functions, name, chart_color='black'):
        super().__init__(functions, name, chart_color)

        if not isinstance(functions, types.FunctionType):
            raise InvalidArgumentInstanceException("Functions should be single function.")

        inspection = getfullargspec(functions)

        if len(inspection[0]) != 2:
            raise InvalidArgumentInstanceException("Functions should be function having 2 parameters.")

    def _method(self, i, results, linspace):
        diff = linspace[i + 1] - linspace[i]
        first = self.functions(results[i], linspace[i])
        second = self.functions(results[i] + first * diff / 2., linspace[i] + diff / 2.)
        return results[i] + second * diff