from math import tanh, exp, fabs, log, sin, tan


x = float(input("Введите значение x = "))
y = float(input("Введите значение y = "))


msg = "Выберите вид функции f(x): tanh(y) = 1, x^5 = 2 "
f = int(input(msg))


if f == 1:
    fx = tanh(y)
elif f == 2:
    fx = x ** 5
else:
    print("Неверный выбор")
    exit()


if fabs(x * y) > 10:
    s = fabs(fx) + log(y)
elif 5 < fabs(x * y) <= 10:
    s = exp(fx + y)
elif fabs(x * y) == 5:
    s = sin(x) + tan(x)
else:
    s = "Значение не может быть вычислено"


print(f"Результат: {s}")
