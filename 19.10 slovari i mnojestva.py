slovar = {1: 11, 2: 22, 3: 33}
slovar[1] = 111
slovar[3] = 333
slovar[4] = 4444  # добавил в словарь новую пару
del slovar[1]
print(type(slovar))

slovar.update({5: 555,
               6: 666})
# key = int(input("введите искомый ключ - "))
# print(slovar.get(key, "такого ключа нет"))
# # возвращает значение по ключу, если ключа нет то НОН или текст после запятой
# #key = int(input("введите удаляемый ключ - "))
# print(slovar.pop(int(input("введите удаляемый ключ - ")), "такого ключа нет"))
print(slovar.keys())
print(slovar.values())
print(slovar.items())
print(slovar)
set_=set(slovar)
print(set_)
print(type(set_), "это уже множество")