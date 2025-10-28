#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys

EPS = 1e-10

if __name__ == '__main__':
    x = float(input("value of x?"))
    S = 0.0
    k = 1
    a = 1.0
    b = 1
    p = x - 1
    if not (0 <= x <= 2):
        print("illegal value of x", file=sys.stderr)

    while abs(a) > EPS:
        b = -b
        a = b * p / (k ** 2)
        p *= x - 1
        S += a
        k += 1

    print(f"f({x}) = {S}")