# На вход программе подается одно слово, записанное в нижнем регистре.
# Напишите программу, которая определяет является ли оно палиндромом

s = input()
if s[::] == s[:: -1]:
    print('YES')
else:
    print('NO')
