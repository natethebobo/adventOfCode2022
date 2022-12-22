#!/usr/bin/env python3

import sys
import re
from collections import deque

fourchars = re.compile('...[ \n]')
move_exp = re.compile("move (?P<count>\d+) from (?P<source>\d+) to (?P<target>\d+)")

datafile = sys.argv[1]
stacks = {}
multimove = True

def load_stacks(line, stacks):
    buckets = fourchars.findall(line)
    for i, bucket in enumerate(buckets):
        i = i + 1
        if i not in stacks:
            stacks[i] = deque()
        if bucket[1] == ' ':
            continue
        stacks[i].appendleft(bucket[1])

def do_move(line, stacks):
    move = move_exp.match(line)
    count = int(move.group('count'))
    source = int(move.group('source'))
    target = int(move.group('target'))
    holder = deque()
    for step in range(int(move.group('count'))):
        item = stacks[source].pop()
        holder.append(item)
    if multimove:
        unload = holder.pop
    else:
        unload = holder.popleft
    while holder:
        stacks[target].append(unload())
    print(stacks)



with open(datafile) as DFILE:
    line = DFILE.readline()
    while line:
        print(line)
        if line.startswith(' 1 '):
            # in the bucket count
            pass
            print("Stacks loaded as")
            print(stacks)
        elif '[' in line:
            load_stacks(line, stacks)
        elif line.startswith('move'):
            do_move(line, stacks)
        line = DFILE.readline()
print(stacks)
print("Topmost is thus:")
line = ""
for i in stacks:
    line += stacks[i].pop()
print(line)
