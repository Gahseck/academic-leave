'''
Задача "Всё не так уж просто":
Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Используя этот список составьте второй список primes содержащий только простые
числа.
А так же третий список not_primes, содержащий все не простые числа.
Выведите списки primes и not_primes на экран (в консоль).
Пункты задачи:
Создайте пустые списки primes и not_primes.
При помощи цикла for переберите список numbers.
Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа
из 1ого цикла.
Отметить простоту числа можно переменной is_prime, записав в неё занчение True
перед проверкой.
В процессе проверки на простоту записывайте числа из списка numbers в списки
primes и not_primes в зависимости от значения переменной is_prime после проверки
(True - в prime, False - в not_prime).
Выведите списки primes и not_primes на экран(в консоль).
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []
for num_ in numbers[1:]:
    flag_prime = True
    for del_ in range(2, num_ - 1):
        if num_ % del_ == 0:
            flag_prime = False
            break
    if flag_prime == True:
        prime.append(num_)
    else:
        not_prime.append(num_)
print('простые числа - ', prime)
print('не простые числа - ', not_prime)
