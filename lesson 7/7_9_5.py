# На вход программе подается натуральное число n. Напишите программу, которая находит цифровой
# корень данного числа. Цифровой корень числа nn получается следующим образом: если сложить все
# цифры этого числа, затем все цифры найденной суммы и повторить этот процесс, то в результате будет
# получено однозначное число (цифра), которое и называется цифровым корнем данного числа.
num = int(input())
while num > 9:
    num_sum = 0
    while num > 0:
        last_digit = num % 10
        num_sum += last_digit
        num = num // 10
    num = num_sum
print(num)
