#!/usr/bin/env python3

import sys
import string

def checkline(line):
    first = line[:len(line)//2]
    second = line[len(line)//2:]
    for char in first:
        if char in second:
            print(f"{first} | {second}")
            print(f"    {char} is in both {first} and {second}")
            return char

def evaluate_dupes(duplicates):
    total = 0
    chars = string.ascii_lowercase + string.ascii_uppercase
    for c in duplicates:
        if c:
            print(f"{c} is index {chars.index(c)}")
            total += chars.index(c) +1
    return total

duplicates = []
with open(sys.argv[1]) as inf:
    line = inf.readline().strip()
    while line:
        duplicates.append(checkline(line))
        line = inf.readline().strip()

print(duplicates)
totals = evaluate_dupes(duplicates)
print(totals)


