#!/usr/bin/python

import sys

# the number of solutions involving Pennies, Nickels, Dimes, and Half-dollars
# can be expressed in O(1) time with MATH
def solve_pndh(amount):
    count = amount // 50 + 1
    n = (amount % 50) // 10 + 1
    solution = count * (50*count*count + 15*count*(2*n - 5) + 6*n*n - 30*n + 25) // 6
    if amount % 10 >= 5:
        solution += (5*count + 2*n - 5) * count // 2
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