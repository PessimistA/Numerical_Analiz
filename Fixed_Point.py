def g(x_):
    return ((x_ * x_ * x_) + (x_ * x_)-3) / 3  # g(x) fonksiyonu

x = 1 
epsilon = 1e-6  
max_iter = 100 
iterasyon = 0

while True:
    x_next = g(x)  


    print(f"İterasyon {iterasyon}: x = {x_next}")

    if abs(x_next - x)< epsilon or iterasyon >= max_iter: 
        break

    x = x_next  
    iterasyon += 1
