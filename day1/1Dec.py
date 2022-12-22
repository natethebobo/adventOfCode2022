#!/usr/bin/env python3

max = 0
maxelf = None
elf = 0
running = 0
elfstack = [0,0,0]
with open("elves") as elves:
	for line in elves.read().splitlines():
		if line:
			running += int(line)
			continue
		# no line, time to compute
		elfstack.append(running)
		elfstack = sorted(elfstack, reverse=True)[0:3]
		running = 0
total = sum(elfstack)
print(elfstack)
print(total)
		
