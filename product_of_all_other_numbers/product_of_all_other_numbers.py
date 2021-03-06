'''
Input: a List of integers
Returns: a List of integers
'''
# def product_of_all_other_numbers(arr):
#     # Simple solution involving division and no allocation
#     product = 1
#     for v in arr:
#         product *= v
    
#     for i in range(len(arr)):
#         arr[i] = product / arr[i]

#     return arr

def product_of_all_other_numbers(arr):
    # product without division
    left = [1] * len(arr)
    right = [1] * len(arr)

    p = 1
    for i in range(len(arr)):
        left[i] = p
        p *= arr[i]
    
    p = 1
    for i in reversed(range(len(arr))):
        right[i] = p
        p *= arr[i]
    
    for i in range(len(arr)):
        arr[i] = left[i] * right[i]
    
    return arr

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
