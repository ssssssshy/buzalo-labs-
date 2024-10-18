x1 = 0
xn = 5
dx = 0.5
a = 0.5
b = 0.7


x = x1
for i in range(int((xn - x1) / dx) + 1):
    f = a * x + b
    print(f"x = {x:.1f}, f(x) = {f:.3f}")
    x += dx
