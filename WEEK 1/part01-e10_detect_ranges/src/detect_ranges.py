#!/usr/bin/env python3

def detect_ranges(L):
    L2 = sorted(L)
    L3 = []
    length = len(L2)

    for i in range(length):
        for j in range(length):
            if L2[i] - L2[j] == -1:
                L3.append(L2[i])

    return L3

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    LX = [2,4,5,6,7,8,10,12,13]
    result = detect_ranges(L)
    print(L)
    print(LX)
    print(result)

if __name__ == "__main__":
    main()
