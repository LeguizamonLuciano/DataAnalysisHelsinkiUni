#!/usr/bin/env python3

def main():

    L = '\n'.join([str((i,x)) for i in range(1,7) for x in range(1,7) if i+x == 5])

    print(L)

if __name__ == "__main__":
    main()
