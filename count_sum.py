a = input("Введите число: ") 
sum = 0 
for i in range(len(a)): 
    if int(a[i]) % 2 == 1: 
        sum += int(a[i])*int(a[i])
print("Сумма чисел: ", sum)
