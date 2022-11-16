from inspect import getfullargspec
from types import FunctionType
from IPython.display import display
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
        Function initializes solve method and chceks if parameters are valid for calculation and displaying.
        :param functions: 2 parameter function representing equations (Could be 2 parameter functions but you need to create own __init__).
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

        self._solution = None
        self._optimal_solution = None

    #region Properites

    @property
    def solution(self):
        return self._solution

    @property
    def optimal_solution(self):
        return self._optimal_solution

    #endregion

    #region Publics

    def solve(self, x0, a, b, n):
        '''
        Method solves equation in range a, b divided in n sectors, with starting value x0.
        :param x0: Starting value
        :param a: Compartment start.
        :param b: Compartment end.
        :param n: Number of intervals.
        :return: Solution class with results.
        '''

        if self.solution != None and self.solution.compare(x0, a, b, n, self.functions):
            return self.solution

        linspace = np.linspace(a, b, n)
        results = np.zeros(n)
        results[0] = x0

        for i in range(n-1):
            results[i+1] = self._method(i, results, linspace)

        self._solution = Solution(linspace, results, self.name, self.functions, self.chart_color)
        self._optimal_solution = self._get_optimal_solution(x0, a, b, n)

        return self.solution

    def draw_plot(self, draw_optimal_solution=False):
        '''
        Method draws plot of the results.
        :param draw_optimal_solution: Indicates drawing optimal solution calculated with NumpySolver.
        '''

        if self.solution == None:
            print('Please solve solution first.')
            return

        plt.plot(self.solution.space,
                 self.solution.results,
                 self.solution.chart_color,
                 label=f'{self.solution.name}')

        if draw_optimal_solution:
            plt.plot(self.optimal_solution.space,
                     self.optimal_solution.results,
                     self.optimal_solution.chart_color,
                     label=f'{self.optimal_solution.name}')

        plt.legend(loc='best')
        plt.xlabel('t')
        plt.grid()
        plt.show()

    def draw_global_error(self):
        if self.solution == None:
            print('Please solve solution first.')
            return

        print(f'Name: {self.name}')
        print(f': {self._get_global_error()}')

    def draw_frame(self):
        if self.solution == None:
            print('Please solve solution first.')
            return

        array = {'t': self.solution.space,
                 'Optimal': self.optimal_solution.results,
                 f'{self.name}': self.solution.results}
        tab = pd.DataFrame(array)
        display(tab)

    #endregion

    #region Privates

    def _method(self, i, results, linspace):
        '''
        Method for calculating i+1 index based on i-th index result.
        :param i: Index of last calculated value.
        :param results: List of results.
        :param linspace: Space of function arguments.
        :return: Result of calculations.
        '''
        raise UnimplementedException("Method must be implemented in order to use it.")

    def _get_global_error(self):
        return max([abs(self.solution.results[i]-self.optimal_solution.results[i]) for i in range(len(self.solution.results))])

    def _get_optimal_solution(self, x0, a, b, n):
        from SolvingMethods.NumpySolver import NumpySolver
        if type(self.functions) == list:
            return NumpySolver(self.functions[0]).solve(x0, a, b, n)

        return NumpySolver(self.functions).solve(x0, a, b, n)

    #endregion

