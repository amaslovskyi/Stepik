# Напишите программу, которая считает стоимость трех компьютеров, состоящих из монитора, системного блока,
# клавиатуры и мыши.
# Формат входных данных
# На вход программе подаётся четыре целых числа, каждое на отдельной строке. В первой строке — стоимость монитора,
# во второй строке — стоимость системного блока, в третьей строке — стоимость клавиатуры и в четвертой строке —
# стоимость мыши.
# Формат выходных данных
# Программа должна вывести одно число – стоимость покупки (трех компьютеров).
monitor, sys_bl, keyboard, mouse = int(input()), int(input()), int(input()), int(input())
coast = (monitor + sys_bl + keyboard + mouse) * 3
print(coast)
