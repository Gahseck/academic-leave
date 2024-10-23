"""
На вход программе подаются 3 целых числа и записываются в переменные
first, second и third соответственно.
Ваша задача написать условную конструкцию (из if, elif, else),
которая выводит кол-во одинаковых чисел среди 3-х введённых.

Пункты задачи:
Если все числа равны между собой, то вывести 3
Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
Если равных чисел среди 3-х вообще нет, то вывести 0
"""
first=input ('Enter the first number - ')
while type(first)==str:
    if first.isnumeric():
        first=int(first)
    else:
        first=input('Введите ЧИСЛО !!! - ')
second=input ('Enter the second number - ')
while type(second)==str:
    if second.isnumeric():
        second=int(second)
    else:
        second=input('Введите ЧИСЛО !!! - ')
third=input ('Enter the second number - ')
while type(third)==str:
    if third.isnumeric():
        third=int(third)
    else:
        third=input('Введите ЧИСЛО !!! - ')
if first==second==third:
    print ('All numbers are equal - 3')
elif first==second or first==third or second==third:
    print ('There are two equal number here - 2')
else:
    print ('There are no equal numbers - 0')