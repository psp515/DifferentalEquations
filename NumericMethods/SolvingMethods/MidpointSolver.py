from Interfaces.ISolver import ISolver


class MidpointSolver(ISolver):
    def __init__(self, functions, name='Midpoint', chart_color='black'):
        super().__init__(functions, name, chart_color)

    def _method(self, i, results, linspace):
        diff = linspace[i + 1] - linspace[i]
        first = self.functions(results[i], linspace[i])
        second = self.functions(results[i] + first * diff / 2., linspace[i] + diff / 2.)
        return results[i] + second * diff