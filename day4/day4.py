#!/usr/bin/env python3

import sys

class DwarfRange(object):

    def __init__(self, rangestr):
        self.start, self.end = rangestr.split('-')
        self.start = int(self.start)
        self.end = int(self.end)

    def is_subset(self, other):
        if self.start <= other.start and self.end >= other.end:
            print(f"{self} contains {other}")
            return True
        if self.start >= other.start and self.end <= other.end:
            print(f"{other} contains {self}")
            return True
        return False

    def overlaps(self, other):
        if self.start <= other.start and self.end >= other.start:
            print(f"{self} overlaps {other}")
            return True
        if other.start <= self.start and other.end >= self.start:
            print(f"{self} is overlapped by {other}")
            return True
        return False

    def __str__(self):
        return f"Dwarf({self.start}-{self.end})"


with open(sys.argv[1]) as INPUT:
    line = INPUT.readline().strip()
    subset_count = 0
    overlaps_count = 0
    while line:
        dwarves = []
        for drange in line.split(','):
            dwarves.append(DwarfRange(drange))
        # if dwarves[0].is_subset(dwarves[1]):
        #     subset_count += 1
        if dwarves[0].overlaps(dwarves[1]):
            overlaps_count += 1
        line = INPUT.readline().strip()
print(f"{subset_count} subsets")
print(f"{overlaps_count} overlaps")

