#!/usr/bin/env python3

def triple(nume):
        return nume*3

def square(numer):
        return numer**2



def main():
    for i in range(1,11):
        y = square(i)
        x = triple(i)
        if y > x:
            break
        else:
            print(f"triple({i})==",x," ",f"square({i})==",y,sep="")


            



if __name__ == "__main__":
    main()
