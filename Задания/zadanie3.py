#!/usr/bin/env python3
#-*- coding: utf-8 -*-

if __name__ == '__main__':
    for i in range(10, 100):
        summ = i % 10 + i // 10
        summ += summ ** 2

        if summ == i:
            print(i)