a = input("Введите атомный номер: ")
if a:
    pH = float(a)
    if pH == 3:
        print("Li")
    elif pH == 25:
        print("Mn")
    elif pH == 80:
        print("Hg")
    else:
        print("Что это?")
else:
    print("Введите атомный номер")
