# Напишите программу для пересчёта величины временного интервала, заданного в минутах,
# в величину, выраженную в часах и минутах.
# Формат входных данных
# На вход программе подаётся целое число – количество минут.
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
minuts = int(input())
hours, left_minuts = minuts // 60, minuts % 60
print(minuts, 'мин', '- это', hours, 'час', left_minuts, 'минут.')
