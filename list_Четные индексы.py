# Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).

a = input().split()
for i in range(0, len(a), 2):
    print(a[i])
    
# a = input()
# s = a.split()
# print(' '.join(s[::2]))