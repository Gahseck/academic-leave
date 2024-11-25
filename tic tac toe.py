area = (['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*'])


def area_printer():
    for i in area:
        print(*i)


area_printer()
print('Добро пожаловать в игру "крестики-нолики')
print('----------------------------------------')
for i in range(1, 10):
    if i % 2 != 0:
        print('-----Ход крестиков (Х)-----')
        column = int(input('Введите номер столбца (1, 2 или 3) - ')) - 1
        line = int(input('Введите номер строки (1, 2 или 3) - ')) - 1
        area[column][line] = 'X'
    else:
        print('-----Ход ноликов (0)-----')
        column = int(input('Введите номер столбца (1, 2 или 3) - ')) - 1
        line = int(input('Введите номер строки (1, 2 или 3) - ')) - 1
        area[column][line] = '0'
# test 123
    area_printer()
