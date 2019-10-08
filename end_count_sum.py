summ = 0 
while True: 
    a = input("Введите число или Стоп для выхода: ") 
    if a == "Стоп": 
        print (summ) 
        break 
    elif a.isdigit()==True: 
        summ += int(a) 
    else: 
        print("Ошибка ввода")
