# Напишите программу для нахождения цифр четырёхзначного числа.
# Формат входных данных
# На вход программе подаётся положительное четырёхзначное целое число.
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
num = int(input())
l_digit, m1_digit, m2_digit, f_digit = num % 10, (num % 100) // 10, (num % 1000) // 100, num // 1000
print('Цифра в позиции тысяч равна', f_digit)
print('Цифра в позиции сотен равна', m2_digit)
print('Цифра в позиции десятков равна', m1_digit)
print('Цифра в позиции единиц равна', l_digit)
