#!/usr/bin/env python3


with open("strategy_guide") as inf:
	input = inf.read().splitlines()


# X means *lose*, 0 pts
# Y means "Tie", 3 pts
# Z means "Win", 6 pts

# if we throw a:
#	Rock:	1 pt
#	Paper:	2 pts
#	Scissors: 3 pts

def brute(line):
	if line == "A X":
		# Lose to Rock ==> Throw Scissors
		return (0 + 3)
	if line == "A Y":
		# Tie with Rock ==> Throw Rock
		return (3 + 1)
	if line == "A Z":
		# Win vs rock, throw Paper
		return (6 + 2)
	if line == "B X":
		return (0 + 1)
	if line == "B Y":
		return (3 + 2)
	if line == "B Z":
		return (6 + 3)
	if line == "C X":
		return (0 + 2)
	if line == "C Y":
		return (3 + 3)
	if line == "C Z":
		return (6 + 1)


def should_throw(line):
	if line == "A Z" or line == "B Y" or line == "C X":
		return "P"
	if line == "A Y" or line == "B X" or line == "C Z":
		return "R"
	if line == "A X" or line == "B Z" or line == "C Y":
		return "S"

def show_outcome(line):
	if "X" in line:
		return "Lose"
	if "Y" in line:
		return "Tie"
	return "Win"

def get_winscore(line):
	if "X" in line:
		return 0
	if "Y" in line:
		return 3
	if "Z" in line:
		return 6

def get_throwscore(line):
	if "R" in line:
		return 1
	if "P" in line:
		return 2
	if "S" in line:
		return 3

total = 0
brute_total = 0
for line in input:
	brute_total += brute(line)
	throw = should_throw(line)
	round = get_winscore(line) + get_throwscore(throw)
	print(f"{line}: {show_outcome(line)}, throw {should_throw(line)}, {brute(line)}? {round} ({get_winscore(line)} + {get_throwscore(throw)})")
	total += round
print(f"brute: {brute_total}, elegant: {total}")
