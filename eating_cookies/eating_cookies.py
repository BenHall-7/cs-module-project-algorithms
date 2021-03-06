'''
Input: an integer
Returns: an integer
'''
# solutions = {
#     0: 1,
#     1: 1,
#     2: 2,
# }

# def eating_cookies(n):
#     global solutions
#     if n in solutions:
#         return solutions[n]
#     n1 = 0
#     n2 = 0
#     n3 = 0
#     if n >= 1:
#         n1 = eating_cookies(n - 1)
#     if n >= 2:
#         n2 = eating_cookies(n - 2)
#     if n >= 3:
#         n3 = eating_cookies(n - 3)
#     total = n1 + n2 + n3
#     solutions[n] = total
#     return total

def eating_cookies(n):
    # 0 1 2 ..
    # 1 1 2 4
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        n1 = 1
        n2 = 1
        n3 = 2
        total = 4
        for _ in range(n - 3):
            n1 = n2
            n2 = n3
            n3 = total
            total = n1 + n2 + n3
        return total

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
