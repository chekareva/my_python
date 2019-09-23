a=input("Выберите фильм: ")
b=input("Выберите дату(сегодня, завтра): ")
c=int(input("Выберите время: "))
d=int(input("Выберите количество билетов: "))
print("Выбрали фильм:",a,"День:",b,"Время:",c,"Количество билетов:",d)
k=1
if b =="Завтра":
    k=0.95
if d >=19:
    k=0.8
if b=="Завтра" and d>=19:
    k=0.75
if a == 'Пятница':
    if c==12:
        print (d*250*k)
    elif c==16:
        print (d*350*k)
    elif c==20:
        print (d*450*k)
elif a=="Чемпионы":
    if c==10:
        print (d*250*k)
    elif c==13:
        print (d*350*k)
    elif c==16:
        print (d*350*k)
elif a=="Пернатая банда":
    if c==10:
        print (d*350*k)
    elif c==14:
        print (d*450*k)
    elif c==18:
        print (d*450*k)
