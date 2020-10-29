#!/usr/bin/env python3

def merge(L1, L2):
    L3 = L1+L2
    L4 = []
    while len(L3) > 0:
        mi = L3[0]
        for i in L3:
            if i < mi:
                mi = i
        L3.remove(min(L3))
        L4.append(mi)
    return L4

def main():
    merge(L1,L2)
    pass

if __name__ == "__main__":
    main()
