# На вход программе подается последовательность целых чисел, каждое число на отдельной строке.
# Концом последовательности является любое отрицательное число. Напишите программу, которая выводит
# сумму всех членов данной последовательности.

num = int(input())
count = 0
while num >= 0:
    sum = int(num)
    count += sum
    num = int(input())
print(count)
