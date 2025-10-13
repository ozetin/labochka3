#!/usr/bin/env python3
#-*- coding: utf-8 -*-

if __name__ == '__main__':
    a1 = int(input("Введите значение a1: "))
    b1 = int(input("Введите значение b1: "))
    c1 = int(input("Введите значение c1: "))

    a2 = int(input("Введите значение a2: "))
    b2 = int(input("Введите значение b2: "))
    c2 = int(input("Введите значение c2: "))

    if a1 == a2 and b1 == b2 and c1 == c2:
        print("Прямые совпадают")

    elif a1 == 0 and b1 == 0 and c1 != 0:
        print("Прямая 1 не существует")

    elif a2 == 0 and b2 == 0 and c2 != 0:
        print("Прямая 2 не существует")

    elif a1 == a2 and b1 == b2:
        print("Прямые параллельны")

    else:
        k1 = -a1 / b1
        b1_new = -c1 / b1

        k2 = -a2 / b2
        b2_new = -c2 / b2

        x = (b2_new - b1_new) / (k1 - k2)
        y = k1 * x + b1_new

        print(f"Точка пересечения: x = {x}, y = {y}")