def f(x_):
    return ((x_ * x_ * x_) - (3 * x_)-2)  

def f1(x_):
    return ((3* x_ * x_) - 3) 

x = 3 
epsilon = 1e-5  
max_iter = 20 
iterasyon = 0

while True:
    x_next =x-( f(x)/f1(x))  


    print(f"İterasyon {iterasyon}: x = {x_next}")

    if abs(x_next - x) < epsilon or iterasyon >= max_iter :
        break

    x = x_next  
    iterasyon += 1
