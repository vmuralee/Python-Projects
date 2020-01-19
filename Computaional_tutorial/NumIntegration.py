# Created by Vinaya Krishnan
# vinaykrishnanmb@gmail.com

import numpy as np
class Integration:
    def __init__(self,a,b,N,user_func):
        self.a = a
        self.b = b
        self.N = N
        self.user_func = user_func
        print(f"The integration is from  {a} to {b} with {N} steps")

   
    def Trapezoidal(self):
        h = (self.b-self.a)/self.N
        #init_list = [user_func(self.a+n*h) for n in range(1,self.N)]
        Value_integral = h*(user_func(self.a)/2+sum([user_func(self.a+n*h) for n in range(1,self.N)])+user_func(self.b)/2)
        print(Value_integral)

    def Rectangular(self):
        h = (self.b-self.a)/self.N
        #init_list = [user_func((j-0.5)*h+self.a) for j in range(1,self.N+1)]
        rectangle_sum = sum([user_func((j-0.5)*h+self.a) for j in range(1,self.N+1)])
        print(h*rectangle_sum)

    def Simpson(self):
        h = (self.b-self.a)/self.N
        init_list = [user_func(self.a+n*h) for n in range(1,self.N)]
        even_list = init_list[::2]
        odd_list = init_list[1::2]
        simpson_sum = h/3*(user_func(self.a)+4*sum(even_list)+2*sum(odd_list)+user_func(self.b))
        print(simpson_sum)

class GaussLegendre(Integration):
    def __init__(self,a,b,N,user_func):
        super().__init__(a,b,N,user_func)
    def Integrate(self):
        roo = {1:[0],2:[0.57735,-0.57735],3:[0,0.774597,-0.774597],
               4:[0.339981,-0.339981,0.861136,-0.861136],5:[0,0.538469,-0.538469,0.90618,-0.90618]}
        om = {1:[0],2:[1,1],3:[0.888889,0.555556,0.555556],
              4:[0.652145,0.652145,0.347855,0.347855],5:[0.568889,0.478629,0.478629,0.236927,0.236927]}
        arg = (self.b+self.a)/2 + np.array(roo[self.N])*((self.b-self.a)/2)
        val = np.array(om[self.N]) * self.user_func(arg)
        return sum(val)*(self.b-self.a)/2

