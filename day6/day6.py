#!/usr/bin/env python3
import sys

FIND='MESSAGE'

with open(sys.argv[1]) as inf:
    lines = inf.read().splitlines()



def check_unique(chars, length=4):
    if len(chars) < length:
        return False
    if len(set(chars)) == length:
        return True
    return False

def start_packet(line):
    for i in range(len(line)):
        if i <= 3:
            continue
        if check_unique(line[i-3:i]):
            return i
    raise Exception("No Packet Detected")

def start_of_message(line):
    for i in range(len(line)):
        if i <= 13:
            continue
        if check_unique(line[i-14: i], 14):
            return i
    raise Exception("No Message Detected")

for line in lines:
    print(line)
    if FIND == 'PACKET':
        print(start_packet(line))
    elif FIND == 'MESSAGE':
        print(start_of_message(line))
    elif FIND == "MESSAGE_AFTER_PACKET":
        packet_start = start_packet(line)
        message_start = start_of_message(line[packet_start:])
        print(packet_start + message_start)
