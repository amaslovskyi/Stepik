# На вход программе подается строка текста. Напишите программу, которая удаляет из нее все
# символы с индексами кратными 3, то есть символы с индексами 0, 3, 6, ....
s = input()
for i in range(len(s)):
    if i %3 != 0:
        print(s[i], end = '')
