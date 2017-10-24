'''
Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.
'''

s = input()
new = ''
for i in range(len(s)):
    if i % 3 != 0:
        new += s[i]
print(new)

# s = ''.join([c for i, c in enumerate(s) if i % 3])