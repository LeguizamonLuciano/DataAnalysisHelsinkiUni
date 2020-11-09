#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    list1 = []
    list2 = []

    f = open("src/rgb.txt", "r").read()
    g = re.findall(r"(\d+)\s+(\d+)\s+(\d+)\s+(.*)",f)

    for i in range(len(g)):
        a = list(g[i])
        list1.append(a)

    for i in range(len(list1)):
        b = "\t".join(list1[i])
        list2.append(b)

    return(list2)


def main():
    pass

if __name__ == "__main__":
    main()
