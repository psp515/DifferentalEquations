from Interfaces.ISolver import ISolver

class EulerSolver(ISolver):
    def __init__(self, functions, name='Euler', chart_color='black'):
        super().__init__(functions, name, chart_color)

    def _method(self, i, results, linspace):
        return results[i] + (linspace[i+1] - linspace[i]) * self.functions(results[i], linspace[i])