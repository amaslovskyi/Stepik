# На вход программе подается одна строка. Напишите программу, которая выводит элементы строки с
# индексами 0, 2, 4, ... в столбик.

string = input()
for i in range(0, len(string), 2):
    print(string[i], end='\n')
