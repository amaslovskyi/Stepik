"""
На обработку поступает последовательность из 7 целых чисел. Известно, что вводимые числа по
абсолютной величине не превышают 10^6. Нужно написать программу, которая подсчитывает и выводит
сумму всех чётных чисел последовательности или 0, если чётных чисел в последовательности нет.
Программист торопился и написал программу неправильно.
Найдите все ошибки в этой программе (их ровно 4). Известно, что каждая ошибка затрагивает только
одну строку и может быть исправлена без изменения других строк.

s = 1
for i in range(1, 7):
    n = input()
    if i % 2 == 0:
        s = s + n
print(s)
"""
sum_num = 0
for i in range(7):
    num = int(input())
    if num % 2 == 0:
        sum_num += num
if sum_num > 0:
    print(sum_num)
else:
    print(0)
