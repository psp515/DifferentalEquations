from sympy import *

x = Symbol('x')
t = Symbol('t')

def f(t, x):
    return -2*x + exp(t)

def f_t(t,x):
    return diff(f(t,x), t)
def f_x(t,x):
    return diff(f(t,x), x)
def f_tx(t,x):
    return diff(f(t,x), t, 1, x, 1)
def f_tt(t,x):
    return diff(f(t,x), t, 2)
def f_xx(t,x):
    return diff(f(t,x), x, 2)
def f1(t,x):
    return f_t(t,x)+f(t,x)*f_x(t,x)

def f2(t, x):
    return f_tt(t,x)+2*f(t,x)*f_tx(t,x)+f_t(t,x)*f_x(t,x)+f(t,x)*(f_x(t,x))**2+(f(t,x))**2*f_xx(t,x)

if __name__ == '__main__':
    print('Program Start')
    print("F:", f(t,x))
    print("F1:", f1(t, x))
    print("F2:", f2(t, x))

