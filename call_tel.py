code = int(input('Введите код города: '))
time = float(input('Введите длительность переговоров(мин)'))
if code:
    if time:
        if code == 343:
            print (15*time)
        elif code == 381:
            print (18*time)
        elif code == 473:
            print (13*time)
        elif code == 485:
            print (11*time)
    else:
        print('Введите время')
else:
print('Введите код города')
