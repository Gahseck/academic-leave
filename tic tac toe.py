area = (('*', '*', '*'), ('*', '*', '*'), ('*', '*', '*'))


def area_printer():
    for i in area:
        print(*i)


area_printer()
print('Добро пожаловать в игру "крестики-нолики')
print('----------------------------------------')
column=int(input('Введите номер столбца (1, 2 или 3) - '))
line=int(input('Введите номер строки (1, 2 или 3) - '))
area[column][line] = 'X'
area_printer()

