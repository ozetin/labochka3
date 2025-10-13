#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys

EPS = 1e-10

if __name__ == '__main__':
    x = float(input("value of x?"))
    S = 0.0
    k = 1
    a = 1.0
    if not (0 <= x <= 2):
        print("illegal value of x", file=sys.stderr)

    while abs(a) > EPS:
        a = ((-1) ** k) * (x - 1) ** k / (k ** 2)
        S += a
        k += 1

    print(f"f({x}) = {S}")