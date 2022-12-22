#!/usr/bin/env python3

import sys
import string


def check_lines(lines):
    possibles = lines[0]
    for line in lines[1:]:
        possibles = compare_two(possibles, line)
    return possibles[0]


def compare_two(l1, l2):
    possible = [char for char in l1 if char in l2]
    return possible


def sum_priority(badges):
    total = 0
    for badge in badges:
        total += priority(badge)
    return total

def priority(char):
    values = string.ascii_lowercase + string.ascii_uppercase
    priority = values.index(char) + 1
    return priority



count = 0
badges = []
with open(sys.argv[1]) as inf:
    lines = [inf.readline().strip() for i in range(0,3)]
    while lines:
        badge = check_lines(lines)
        badges.append(badge)
        lines = [inf.readline().strip() for i in range(0,3)]
        if lines[2] == '':
            if lines[0] != '':
                raise Exception("Not enough lines!")
            break
        count += 1
print(sum_priority(badges))


