#!/usr/bin/env python3
'''
Prints a b"string" (bytes object), reads a char from stdin
and prints the same (or not :)) string again
'''

import sys

s = b"Holberton"
print("{} at 0x{:x}".format(s, id(s)))

while sys.stdin.read(1):
    print("{} at 0x{:x}".format(s, id(s)))
