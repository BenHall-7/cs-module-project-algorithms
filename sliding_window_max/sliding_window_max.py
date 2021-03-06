'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

from collections import deque

def sliding_window_max(nums, k):
    results = []
    # contains the indeces of the elements for which
    # all proceeding elements have a smaller value.
    # leftmost value is largest; rightmost is smallest
    seq = deque(maxlen=k)
    def insert(i):
        nonlocal seq, nums
        n = nums[i]
        while len(seq) > 0 and n >= nums[seq[-1]]:
            seq.pop()
        seq.append(i)

    for i in range(0,k):
        insert(i)

    results.append(nums[seq[0]])

    for i in range(k, len(nums)):
        # if the last/biggest number fell out of the window, remove it
        if seq[0] <= i - k:
            seq.popleft()
        insert(i)
        results.append(nums[seq[0]])
    
    return results

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
