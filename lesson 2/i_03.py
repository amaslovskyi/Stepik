# Напишите программу, вычисляющую объём куба и площадь его полной поверхности, по введённому значению длины ребра.
# Формат входных данных
# На вход программе подается одно целое число – длина ребра.
# Формат выходных данных
# Программа должна вывести текст и числа в соответствии с условием задачи.
# Примечание. Объём куба и площадь полной поверхности можно вычислить по формулам V = a^3,  S=6a^2

r_lenght = int(input())
volume = r_lenght ** 3
sa = 6 * (r_lenght ** 2)
print('Объем =', volume,)
print('Площадь полной поверхности =', sa)
