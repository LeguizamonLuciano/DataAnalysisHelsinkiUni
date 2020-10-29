#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):

    d = (math.sqrt(b**2-4*a*c))

    x = (-b+d)/(2*a)
    y = (-b-d)/(2*a)

    return (x,y)


def main():
    print(solve_quadratic(2,10,-3))

if __name__ == "__main__":
    main()
