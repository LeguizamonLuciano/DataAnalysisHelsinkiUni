#!/usr/bin/env python3
from functools import reduce
def sum_equation(L):

    b = str(L).strip("[]").replace(", "," + ")

    if len(L) > 0:
        result = str(reduce(lambda x,y:x+y,L))
        a = b+" = "+result
        return(a)  
    else:
        return("0 = 0")

def main():
    pass

if __name__ == "__main__":
    main()
