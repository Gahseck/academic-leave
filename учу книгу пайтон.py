# задача 2-переставить элементы и посчитать длину списка
# listing = []
# while 1==1:
#     element = input('Введите элемент, если список закончился введите "1" - ')
#     if element != '1':
#         listing.append(element)
#     else: break
# print(listing)
# listing.reverse()
# print(listing)
# print('длина списка - ',len(listing))


# задача 3. сортировка по возрастанию и убыванию
dictionary={}
while 1==1:
    key=input('введите ключ, если выход из словаря введите "0" - ')
    if key != '0':
        item=input('введите элемент - ')
        dictionary.update({key:item})
    else: break
print("создали словарь - ", dictionary)
dictionary=dictionary.items()
print("преоброзовали словарь в список кортежей - ", dictionary)
dictionary=sorted(dictionary)
print("отсортировали список кортежей по алфавиту - ", dictionary)
dictionary1=dict(dictionary)
print("решение 1 - словарь по алфавиту - ", dictionary1)
dictionary2=reversed(dictionary)
dictionary3=dict(dictionary2)
print("решение 2 - словарь по убыванию - ", dictionary3)
