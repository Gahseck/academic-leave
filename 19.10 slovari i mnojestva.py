slovar = {1: 11, 2: 22, 3: 33}
slovar[1] = 111
slovar[3] = 333
slovar[4] = 4444  # добавил в словарь новую пару
del slovar[1]
print(type(slovar))
slovar.update({5:555,
               6:666})
print(slovar.get(1, "такого ключа нет")) # возвращает значение по ключу, если ключа нет то НОН или текст после запятой
print(slovar)
