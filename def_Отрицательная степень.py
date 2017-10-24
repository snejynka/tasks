# Дано действительное положительное число a и целоe число n.
# Вычислите a^n. Решение оформите в виде функции power(a, n).
# Стандартной функцией возведения в степень пользоваться нельзя.

def power(a, n):
    stepen = 1
    for i in range(abs(n)):
        stepen *= a
    if n >= 0:
        return stepen
    else:
        return 1 / stepen

print(power(float(input()), int(input())))