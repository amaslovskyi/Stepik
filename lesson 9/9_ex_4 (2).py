# На вход программе подается строка текста. Напишите программу, которая выводит индекс второго
# вхождения буквы «f». Если буква «f» встречается только один раз, выведите число -1, а если
# не встречается ни разу, выведите число -2.
s = input()
if s.count('f') < 1:
    print(-2)
elif s.count('f') == 1:
    print(-1)
else:
    print(s.replace('f', '_', 1).find('f'))
