'''
По данному целому числу N распечатайте все квадраты натуральных чисел, 
не превосходящие N, в порядке возрастания.
'''

n = int(input())
a = 1
while a ** 2 <= n:
    print(a ** 2, end =" ")
    a += 1