class Roots:
    def __init__(self,x_low,x_up,max_iter):
        self.x_low     = x_low
        self.x_up      = x_up
        self.max_iter = max_iter
    def user_func(self,x):
        return x*x-2
    def user_func_derv(self,x):
        return 2*x
    
    def Secant(self):
        for i in range(self.max_iter):
            x_2 = (self.user_func(self.x_up)*self.x_low-self.user_func(self.x_low)*self.x_up)/(self.user_func(self.x_up)-self.user_func(self.x_low))
            self.x_low = self.x_up
            self.x_up = x_2
        print(x_2)
    def NewtonRaphson(self):
        a = self.x_up
        for i in range(self.max_iter):
            a = a - self.user_func(a)/self.user_func_derv(a)
        print(a)

    def Bisection(self):
        a,b=self.x_low,self.x_up
        x_mid=self.x_low
        for i in range(self.max_iter):
            x_mid = (a+b)/2
            condi = self.user_func(a)*self.user_func(x_mid)
            if(condi < 0):
                b=x_mid
            #print(b,'  ',x_mid)
            elif(condi > 0):
                a = x_mid
            #print(a,'  ',x_mid)
            else:
                exit(1)
        print(x_mid)
