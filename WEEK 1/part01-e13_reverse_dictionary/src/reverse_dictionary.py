#!/usr/bin/env python3

def reverse_dictionary(d):

    dicti = {}
 
    for key, values in d.items():
        for i in values:
            dicti.setdefault(i, []).append(key)
            
    return(dicti)

def main():
    pass

if __name__ == "__main__":
    main()
