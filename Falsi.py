import math
from math import exp
def f(x_):
    return (x_*x_*x_)-(2*x_)-3

epsilon = 1e-5
a=0
b=2  
interval =[a,b]
max_iter = 20 
iterasyon = 0

while True:
    if(f(a)*f(b)<0):
        x_next =( ((a*f(b))-(b*f(a)))/(f(b)-f(a)))  


        print(f"İterasyon {iterasyon}: x = {x_next}")

        if abs(b-a) < epsilon or iterasyon >= max_iter :
            break
        if(f(x_next)*f(b)<0):
            a = x_next
        if(f(x_next)*f(a)<0):
            b=x_next
        iterasyon += 1
