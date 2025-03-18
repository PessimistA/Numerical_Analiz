import math
from math import exp
def f(x_):
    return math.exp(-2*x_) -x_


x0 =1
x_1=0 
epsilon = 1e-5  
max_iter = 20 
iterasyon = 0

while True:
    x_next =x0-( (f(x0)*(x0-x_1))/(f(x0)-f(x_1)))  


    print(f"İterasyon {iterasyon}: x = {x_next}")

    if abs(x_next - x0) < epsilon or iterasyon >= max_iter :
        break
    x_1=x0
    x0 = x_next  
    iterasyon += 1
