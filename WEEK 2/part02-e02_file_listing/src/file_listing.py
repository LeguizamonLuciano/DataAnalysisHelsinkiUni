#!/usr/bin/env python3

import re

def file_listing(filename="src/listing.txt"):
    list1 = []
    list2 = []
    f = open("src/listing.txt", "r").read()
    f = ''.join(f)
    a = re.findall(r"(\d+)\s*(\w+)\s+(\d+)\s(\d+)\:(\d+)\s(.*)", f)

    for i in range(len(a)):
        w = list(a[i])
        list1.append(w)

    for i in range(len(list1)):
        list1[i][0] = int(list1[i][0])
        list1[i][2] = int(list1[i][2])
        list1[i][3] = int(list1[i][3])
        list1[i][4] = int(list1[i][4])

    for i in range(len(list1)):
        t = tuple(list1[i])
        list2.append(t)

    return list2

def main():
    pass

if __name__ == "__main__":
    main()
