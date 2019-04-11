from math import *
class Backward:
    def __init__(self, f, h=e-9): 
        self.f, self.h = f, h 
    def __call__(self, x): 
        h, f = self.h, self.f 
        return (f(x) - f(x-h))/h # finite difference
dsin = Backward(sin) 
e = dsin(0) - cos(0); 
print ('error:', e) 
dexp = Backward(exp, h=e-7) 
e = dexp(0) - exp(0); 
print ('error:', e)
