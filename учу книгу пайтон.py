''' задача Создать учетные данные
-создать словарь1
-задать логин
-проверить логин на индивидуальность в словаре
-сохранить логин в словаре2
-задать пароль
-проверить пароль
-сохранить пароль в словаре2
слияние словарей
'''
from unicodedata import numeric

dictionary1={'x':11}
# создаем логин
while 1>0:
    login=input('Ведите новый логин - ')
    if login not in dictionary1:
        dictionary1[login]=0
        break
    else:
        print("Такой логин уже существует")
        continue
# создаем пароль
while 1:
    parol=input('Ведите новый пароль (необходимо не менее 8 прописных,строчных буквы и цифр) - ')
    parol_list=list(parol)
    #lengts=len(parol)
    if len(parol)<8:
        print("вы ввели недостаточное количество символов")
        continue
    degree_of_protection=[]
    lower=0
    title=0
    numer=0
    for i in parol:
        if i.islower():
            lower += 1
            break
    for i in parol:
        if i.istitle():
            title += 1
            break
    for i in parol:
        if i.isnumeric():
            numer += 1
            break
    if numer+title+lower==3:
        print('Вы ввели достаточно сложный пароль')
        dictionary1[login] = parol
        break
    else:
        if lower==0: degree_of_protection.append('строчные буквы')
        if title==0: degree_of_protection.append('прописные буквы')
        if numer==0: degree_of_protection.append('цифры')
        print('Вы ввели недостаточно сложный пароль\n'
              'необходимо использовать - ',degree_of_protection)

        continue

print(dictionary1)
