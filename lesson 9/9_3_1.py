# На вход программе подается строка состоящая из имени и фамилии человека, разделенных одним пробелом.
# Напишите программу, которая проверяет, что имя и фамилия начинаются с заглавной букв

s = input()
if s == s.title():
    print('YES')
else:
    print('NO')
