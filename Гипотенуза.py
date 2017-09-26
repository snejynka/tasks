'''
Дано два числа a и b. 
Выведите гипотенузу треугольника с заданными катетами.
'''

from math import sqrt

a = int(input())
b = int(input())

print(sqrt(a ** 2 + b ** 2))