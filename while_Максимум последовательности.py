'''
Последовательность состоит из натуральных чисел и завершается числом 0.
Определите значение наибольшего элемента последовательности.
'''

n = int(input())
max_element= 0
while n != 0:
    if n > max_element:
        max_element = n
    n = int(input())
print(max_element)