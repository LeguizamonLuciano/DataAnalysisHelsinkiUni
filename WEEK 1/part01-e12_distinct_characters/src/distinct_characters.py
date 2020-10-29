#!/usr/bin/env python3

def distinct_characters(L):
    dictio = {}
    for i in range(len(L)):
        x = "".join(L[i])
        f = set(x)
        dictio[L[i]] = len(f)

    return dictio

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
