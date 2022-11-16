from inspect import getfullargspec
from types import FunctionType

from wand.display import display

from Utils.Solution import Solution
from Utils.InvalidArgumentInstanceException import InvalidArgumentInstanceException
from Utils.UnimplementedException import UnimplementedException

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class ISolver:
    '''
    Interface created for implementing in numeric methods that calculates 2 parameter functions.
    Class should be representing a mathematical function, that can take different parameters to get required data.
    '''
    def __init__(self, functions, name, chart_color):
        '''
        Function initializes solve method and chceks if parameters are valid for calculation and displaying in matplotlib.pyplot.
        :param functions: 2 parameter function representing equations.
        :param name: Name to be displayed.
        :param chart_color: Default color on chart.
        '''
        if not isinstance(functions, FunctionType):
            raise InvalidArgumentInstanceException("Functions should be single function.")

        inspection = getfullargspec(functions)

        if len(inspection[0]) != 2:
            raise InvalidArgumentInstanceException("Functions should be function having 2 parameters.")

        if not isinstance(chart_color, str):
            raise InvalidArgumentInstanceException("Chart color should be string.")

        self.chart_color = chart_color
        self.functions = functions
        self.name = name
        self.solution = None
        self.optimal_solution = None

    def _method(self, i, results, linspace):
        '''
        Method for calculating i+1 index based on i-th index result.
        :param i: Index of last calculated value.
        :param results: List of results.
        :param linspace: Space of function arguments.
        :return: Result of calculations.
        '''
        raise UnimplementedException("Method must be implemented in order to use it.")

    def solve(self, x0, a, b, n):
        '''
        Method solves equation in range a,b divided in n sectors, with starting value x0.
        :param x0: Starting value
        :param a: Compartment start.
        :param b: Compartment end.
        :param n: Number of intervals.
        :return: Solution class with results.
        '''

        if self.solution != None and self.solution.compare(x0, a, b):
            return self.solution

        linspace = np.linspace(a, b, n)
        results = np.zeros(n)
        results[0] = x0

        for i in range(n-1):
            results[i+1] = self._method(i, results, linspace)

        self.solution = Solution(linspace, results, self.name, self.functions, self.chart_color)

        return self.solution

    def draw_plot(self, x0, a, b, n, draw_optimal_solution=False):
        '''
        Method draws plot of the results.
        :param x0: Starting value
        :param a: Compartment start.
        :param b: Compartment end.
        :param n: Number of intervals.
        :param draw_optimal_solution: Indicates drawing optimal solution calculated with NumpySolver.
        '''
        solution = self.solve(x0, a, b, n)
        plt.plot(solution.space, solution.results, solution.chart_color, label=f'{solution.name}')

        if draw_optimal_solution:
            optimal_solution = self._get_optimal(x0, a, b, n)
            plt.plot(optimal_solution.space, optimal_solution.results, optimal_solution.chart_color, label=f'{optimal_solution.name}')

        plt.legend(loc='best')
        plt.xlabel('t')
        plt.grid()
        plt.show()


    def get_global_error(self, x0=None, a=None, b=None, n=None):
        '''
        Method compares solution with optimal solution calculated with NumpySolver.
        :param x0: Starting value
        :param a: Compartment start.
        :param b: Compartment end.
        :param n: Number of intervals.
        :returns: Biggest difference between optimal value and calculated.
        '''
        solution = self.solve(x0, a, b, n).results
        optimal_solution = self._get_optimal(x0, a, b, n).results

        return max([abs(solution[i]-optimal_solution[i]) for i in range(n)])

    def draw_frame(self, x0, a, b, n):
        solution = self.solve(x0, a, b, n).results
        optimal_solution = self._get_optimal(x0, a, b, n).results
        array = {'t': solution.space, 'Optimal': optimal_solution.results, f'{self.name}': solution.results}
        tab = pd.DataFrame(array)
        display(tab)

    def _get_optimal(self, x0, a, b, n):
        from SolvingMethods.NumpySolver import NumpySolver

        if self.optimal_solution is None or not self.optimal_solution.compare(x0, a, b, n, self.functions):
            self.optimal_solution = NumpySolver(self.functions).solve(x0, a, b, n)

        return self.optimal_solution


