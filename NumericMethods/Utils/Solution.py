


class Solution():
    def __init__(self, space, results, name, chart_color='black'):
        self._space = space
        self._results = results
        self._name = name
        self._chart_color = chart_color

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

    def compare_arguments(self, x0, a, b):
        return x0 == self.results[0] and \
               self.space[0] == a and \
               self.space[-1] == b