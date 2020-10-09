#!/usr/bin/python

import sys

# the number of solutions involving Pennies, Nickels, Dimes, and Half-dollars
# can be expressed in O(1) time with MATH
def solve_pndh(amount):
    a = amount // 50 + 1
    b = (amount % 50) // 10 + 1
    solution = a * (50*a*a + 15*a*(2*b - 5) + 6*b*b - 30*b + 25) // 6
    if amount % 10 >= 5:
        solution += (5*a + 2*b - 5) * a // 2
    return solution

def making_change(amount, denominations):
    num_solutions = 0
    for num_quarters in range(amount // 25 + 1):
        rem = amount - num_quarters * 25
        num_solutions += solve_pndh(rem)
    return num_solutions


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")