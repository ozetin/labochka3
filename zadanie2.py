a1 = int(input("Введите значение а1: "))
b1 = int(input("Введите значение b1: "))
c1 = int(input("Введите значение c1: "))
a2 = int(input("Введите значение а2: "))
b2 = int(input("Введите значение b2: "))
c2 = int(input("Введите значение c2: "))
if a1 == a2:
    if b1 == b2 and c1 == c2:
        print("Прямые совпадают")
    elif a1 == 0 and b1 ==0 and c1 != 0:
        print("Прямой 1 не существует")
    elif a2 == 0 and b2 == 0 and c2 != 0:
        print("Прямой 2 не существует")
    else:
        print("Прямые параллельны")
else:
    a1_2 = a1 / b1
    c1_2 = c1 / b1
    a2_2 = a2 / b2
    c2_2 = c2 / b2
    a = a1_2 - a2_2
    c = c1_2 - c2_2
    x = -c / a
    y = -(a1 * x + c1) / b1
    print(x, y)