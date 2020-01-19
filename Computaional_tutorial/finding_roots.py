import numpy as np
from math import sqrt,tan
from sympy import Symbol,diff,evalf

class Roots:
    def __init__(self,x_low,x_up,max_iter,user_func):
        self.x_low     = x_low
        self.x_up      = x_up
        self.max_iter = max_iter
        self.user_func = user_func
    
    def user_func_derv(self,x):
        a = Symbol('x')
        val = diff(user_func(a)).subs(a,x)
        return val
    def Help(self):
        print('The arguments are (x_low,x_up and maximum iteration)')
        print('\nMethods available are Secant,NewtonRaphson and Bisection methods')
        print('\n')
    def Secant(self):
        for i in range(self.max_iter):
            x_2 = (user_func(self.x_up)*self.x_low-user_func(self.x_low)*self.x_up)/(user_func(self.x_up)-user_func(self.x_low))
            self.x_low = self.x_up
            self.x_up = x_2
        return x_2
    def NewtonRaphson(self):
        a = self.x_up
        for i in range(self.max_iter):
            a = a - user_func(a)/self.user_func_derv(a)
        return a.evalf()

    def Bisection(self):
        a,b=self.x_low,self.x_up
        x_mid=self.x_low
        for i in range(self.max_iter):
            x_mid = (a+b)/2
            condi = user_func(a)*user_func(x_mid)
            if(condi < 0):
                b=x_mid
            #print(b,'  ',x_mid)
            elif(condi > 0):
                a = x_mid
            #print(a,'  ',x_mid)
            else:
                exit(1)
        print(x_mid)
