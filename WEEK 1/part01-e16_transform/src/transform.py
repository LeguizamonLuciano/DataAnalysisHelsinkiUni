#!/usr/bin/env python3

def transform(s1, s2):
    x=s1.split()
    o=s2.split()

    w=[]
    m=[]
    z = [w.append(int(i)) for i in x if i != ' ']
    y = [m.append(int(i)) for i in o if i != ' ']

    a = map(int,w)
    b = map(int,m)

    f = list(zip(w,m))

    lastone = [(x*y) for x,y in f]

    return lastone

def main():
    pass

if __name__ == "__main__":
    main()
