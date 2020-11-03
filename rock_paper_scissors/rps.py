#!/usr/bin/python

import sys

NAMES = [
  "rock",
  "paper",
  "scissors"
]

def rock_paper_scissors(n):
  global NAMES
  res = []
  for i in range(3 ** n):
    throws = [0] * n
    for move_num in reversed(range(n)):
      throws[move_num] = NAMES[i % 3]
      i //= 3
    res.append(throws)
  return res

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')