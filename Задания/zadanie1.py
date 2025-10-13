#!/usr/bin/env python3
#-*- coding: utf-8 -*-

if __name__ == '__main__':
    N = int(input("Введите число экзаменов: "))

    if N == 1:
        print(f"Мы успешно сдали {N} экзамен")

    elif 1 < N < 5:
        print(f"Мы успешно сдали {N} экзамена")

    elif 5 <= N <= 20:
        print(f"Мы успешно сдали {N} экзаменов")

    else:
        print("Нужно ввести число от 1 до 20")