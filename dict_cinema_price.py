
cinema = { 
    'Пятница': {'time_price': {12: 250, 16: 350, 20: 450}, 'genre': 'комедия', 'limit': 16}, 
    'Чемпионы': {'time_price': {10: 250, 13: 350, 16: 350}, 'genre': 'спорт', 'limit': 16}, 
    'Пернатая банда': {'time_price': {10: 350, 14: 450, 18: 450}, 'genre': 'мультфильм', 'limit': 6} 
    } 
print('Билеты есть только на сегодня и завтра') 
for key in cinema: 
    print(key) 
a=input("Выберите фильм: ") 
for key in cinema[a]['время']: 
    print(key) 
b=input("Выберите дату(сегодня, завтра): ") 
c=int(input("Выберите время: ")) 
d=int(input("Выберите количество билетов: ")) 
price=cinema[a]['время'][c]*d 
if b=='завтра' and d>=19: 
    price *=0.75 
elif b!='завтра' and d>=19: 
    price *=0.8 
elif b=='завтра' and d<19: 
    price *=0.95 
print('Итого: ',price)
