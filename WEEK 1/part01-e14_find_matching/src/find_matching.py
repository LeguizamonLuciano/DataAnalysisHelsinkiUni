#!/usr/bin/env python3

def find_matching(L, pattern):

    enumeratedL = list(enumerate(L))
    matched=[]
    
    for i in range(len(enumeratedL)):
        if pattern in enumeratedL[i][1]:
            matched.append(i)
    return matched

def main():
    
    pass

if __name__ == "__main__":
    main()
