# На вход программе подается одна строка. Напишите программу, которая выводит сообщение «Цифра»
# (без кавычек), если строка содержит цифру. В противном случае вывести сообщение «Цифр нет» (без кавычек).

s = input()
flag = 'Цифр нет'
for i in range(len(s)):
    if s[i] in '0123456789':
        flag = 'Цифра'
print(flag)

