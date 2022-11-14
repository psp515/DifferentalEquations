import types
from inspect import getfullargspec

from Interfaces.ISolvable import ISolvable
from Utils.InvalidArgumentInstanceException import InvalidArgumentInstanceException


class RungeKuttSolver(ISolvable):
    def __init__(self, functions, method_name):
        super().__init__(functions, method_name)

        if not isinstance(functions, types.FunctionType):
            raise InvalidArgumentInstanceException("Functions should be single function.")

        inspection = getfullargspec(functions)

        if len(inspection[0]) != 2:
            raise InvalidArgumentInstanceException("Functions should be function having 2 parameters.")

    def _method(self, i, results, linspace):
        diff = linspace[i + 1] - linspace[i]
        #TOCHECK
        first = self.functions(results[i], linspace[i])
        second = self.functions(results[i] + first * diff / 2., linspace[i] + diff / 2.)
        third = self.functions(results[i] + second * diff / 2., linspace[i] + diff / 2.)
        fourth = self.functions(results[i] + third * diff, linspace[i] + diff)
        return results[i] + (diff / 6.) * (first + 2*second + 2*third + fourth)