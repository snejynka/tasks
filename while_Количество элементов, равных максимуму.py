'''
Последовательность состоит из натуральных чисел и завершается числом 0.
Определите, сколько элементов этой последовательности равны ее наибольшему элементу.
'''

n = int(input())
max_element= 0
i = 0
while n != 0:
    if n > max_element:
        max_element = n
        i = 1
    elif n == max_element:
        i += 1
    n = int(input())
print(i)