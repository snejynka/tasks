'''
Определите сумму всех элементов последовательности, завершающейся числом 0. 
В этой и во всех следующих задачах числа, следующие за первым нулем, учитывать не нужно.
'''

n = int(input())
sum = 0
while n != 0:
    sum += n
    n = int(input())
print(sum)