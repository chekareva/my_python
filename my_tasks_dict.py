tasks=[]
while True:
    q=int(input('Простой todo:\n 1. Добавить задачу\n 2. Вывести список задач\n 3. Выход\n\nУкажите число: '))
    if q=='1':
        a=input('Сформулируйте задачу: ') 
        b=input('Добавьте категорию к задаче: ') 
        d=input('Добавьте время к задаче: ') 
        todo+=[{'a':a, 'b':b, 'd':d}]
    elif q=='2':
        for i in tasks:
             print('Задача: ',i['a'],' Категория: ',i['b'],' Время: ', i['d'])
    elif q=='3':
        break
