import types
from inspect import  getfullargspec

from Interfaces.ISolvable import ISolvable
from Utils.InvalidArgumentInstanceException import InvalidArgumentInstanceException


class EulerSolver(ISolvable):
    def __init__(self, functions, method_name):
        super().__init__(functions, method_name)

        if not isinstance(functions, types.FunctionType):
            raise InvalidArgumentInstanceException("Functions should be single function.")

        inspection = getfullargspec(functions)

        if len(inspection[0]) != 2:
            raise InvalidArgumentInstanceException("Functions should be function having 2 parameters.")

    def _method(self, i, results, linspace):
        return results[i] + (linspace[i+1] - linspace[i]) * self.functions(results[i], linspace[i])