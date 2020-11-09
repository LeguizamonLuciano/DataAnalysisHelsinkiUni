#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    regexFindall = re.findall(r"\[(\s*[-+]?\d+\s*)\]",s)
    regexList = [int(x) for x in regexFindall]

    return regexList

def main():
    pass

if __name__ == "__main__":
    main()
