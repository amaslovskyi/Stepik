"""
На вход программе подается одна строка. Напишите программу, которая выводит:

третий символ этой строки;
предпоследний символ этой строки;
первые пять символов этой строки;
всю строку, кроме последних двух символов;
все символы с четными индексами;
все символы с нечетными индексами;
все символы в обратном порядке;
все символы строки через один в обратном порядке, начиная с последнего.
"""

s = input()
print(s[2], s[-2], s[:5], s[:-2], s[::2], s[1::2],s[::-1], s[::-2], sep='\n')