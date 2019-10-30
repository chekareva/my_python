def sm(a,b): 
    return a+b 
def rs(a,b): 
    return a-b 
def ym(a,b): 
    return a*b 
def dl(a,b): 
    return a/b
A={'+':sm,'-':rs,'*':ym,'/':dl}
try: 
    a = int(input('Введите первое число: ')) 
    b = int(input('Введите второе число: '))
    c = int(input('Введите оператор: '))
    print(A[c](a,b)) 
except ZeroDivisionError: 
    print('Ошибка деления на ноль!') 
except ValueError: 
    print('Ошибка преобразования типов!') 
except KeyError: 
    print('Ошибка неверного оператора!')
