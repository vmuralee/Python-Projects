# Created by Vinaya Krishnan
# vinaykrishnanmb@gmail.com

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

