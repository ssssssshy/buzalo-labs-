from math import sqrt, fabs, exp, sin


x = float(input("Введите значение x = "))
y = float(input("Введите значение y = "))


if x + pow(fabs(y), 1 / 4) > 0:

    a1 = 2 - x
    a2 = sqrt(x + pow(fabs(y), 1 / 4))
    a3 = exp(x - 1 / sin(x))


    z = a1 * a2 * a3
    print(f"Результат: {z}")
else:
    print("Значение выражения не может быть вычислено")
