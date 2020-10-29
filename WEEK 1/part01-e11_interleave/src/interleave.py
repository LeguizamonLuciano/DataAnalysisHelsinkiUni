#!/usr/bin/env python3

def interleave(*lists):
    interList3 = list(zip(*lists)) #Zippeo los elementos en una lista grande
    interList4 = [] #La uso para crear la nueva lista de elementos zipeados

    for i in interList3:#Le saco las tuplas y las paso a elementos de interList4
        for x in i:
            interList4.append(x) 

    return interList4

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
