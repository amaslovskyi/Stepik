# Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется средней
# по величине цифре. Напишите программу, которая определяет интересное число или нет. Если число
# интересное, следует вывести – «Число интересное» иначе «Число неинтересное».
num = int(input())
num_l, num_m, num_f = num % 10, (num % 100) // 10, num // 100
num_min, num_max = min(num_l, num_m, num_f), max(num_l, num_m, num_f)
num_middle = (num_l + num_m + num_f) - (num_min + num_max)
if num_max - num_min == num_middle:
    print('Число интересное')
else:
    print('Число неинтересное')
