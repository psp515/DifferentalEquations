


class Solution():
    def __init__(self, space, results, name, functions, chart_color='black'):
        self._space = space
        self._results = results
        self._name = name
        self._chart_color = chart_color
        self._functions = functions

    @property
    def functions(self):
        return self._functions

    @property
    def space(self):
        return self._space

    @property
    def results(self):
        return self._results

    @property
    def name(self):
        return self._name

    @property
    def chart_color(self):
        return self._chart_color

    def compare(self, x0, a, b, n, functions):
        '''
        Function indicates whether solution is solution of equations with following parameters:
        :param x0: Starting value
        :param a: Compartment start.
        :param b: Compartment end.
        :param n: Number of intervals.
        :param functions: Functions of the equation.
        :return: True if solution is solution of this equations else false
        '''
        return x0 == self.results[0] and \
               self.space[0] == a and \
               self.space[-1] == b and \
               len(self.space) == n and \
               self.functions == functions