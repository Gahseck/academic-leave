stroka='voina i mir'
print(stroka.upper())
print(stroka.lower())
print(stroka[0].upper()+stroka[1:-1]+stroka[0].upper())
print(stroka.islower())
print(stroka[1].islower())
print(stroka.isupper())
print(stroka[1].isupper())
print(stroka.replace('voina','xxx'))
print(min(stroka))#не знаю что делает, точнее не понял
print(stroka.partition('i'))
print(id(stroka))
izmeneniya=str.maketrans('voina ', '12345=')
print(stroka.translate(izmeneniya))
print(stroka)

















