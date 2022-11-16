from Interfaces.ISolver import ISolver

class RungeKutt4Solver(ISolver):
    def __init__(self, functions, name='Runge-Kutt-4', chart_color='black'):
        super().__init__(functions, name, chart_color)

    def _method(self, i, results, linspace):
        diff = linspace[i + 1] - linspace[i]

        first = self.functions(results[i], linspace[i])
        second = self.functions(results[i] + first * diff / 2., linspace[i] + diff / 2.)
        third = self.functions(results[i] + second * diff / 2., linspace[i] + diff / 2.)
        fourth = self.functions(results[i] + third * diff, linspace[i] + diff)

        return results[i] + (diff / 6.) * (first + 2*second + 2*third + fourth)