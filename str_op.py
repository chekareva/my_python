s = "У лукоморья 123 дуб зеленый 456"
print("Позиция в строке буквы я: ", s.find('я'))
print("Буква у встречается ", s.count('у'), "раз в строке")
if s.isalpha()== False:
    print (s.upper())
if len(s) > 4:
    print (s.lower())
print ("о" + s[1:])

