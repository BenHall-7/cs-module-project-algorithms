'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    appeared_once = set()
    for v in arr:
        if v in appeared_once:
            appeared_once.remove(v)
        else:
            appeared_once.add(v)
    
    return next(iter(appeared_once))


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")