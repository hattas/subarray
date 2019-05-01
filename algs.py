import numpy as np

def _find_max_crossing_subarray(A, low, mid, high):
    '''p71 Introduction To Algorithms'''
    left_sum = -np.inf
    sum_ = 0
    for i in range(mid, low-1, -1):
        sum_ = sum_ + A[i]
        if sum_ > left_sum:
            left_sum = sum_
            max_left = i
    right_sum = -np.inf
    sum_ = 0
    for j in range(mid+1, high+1):
        sum_ = sum_ + A[j]
        if sum_ > right_sum:
            right_sum = sum_
            max_right = j
    return (max_left, max_right, left_sum + right_sum)

def find_maximum_subarray(A, low=None, high=None, return_type=dict):
    '''p72 Introduction To Algorithms'''
    if low == None:
        low = 1 # low is 1 because A[0] is NaN
    if high == None:
        high = len(A) - 1
    
    if high == low:
        return_low, return_high, return_sum = low, high, A[low]
    elif high < low:
        return_low, return_high, return_sum = low, high, 0
    else:
        mid = int(np.floor((low + high) / 2))
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid, tuple)
        right_low, right_high, right_sum = find_maximum_subarray(A, mid + 1, high, tuple)
        cross_low, cross_high, cross_sum = _find_max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return_low, return_high, return_sum = left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return_low, return_high, return_sum = right_low, right_high, right_sum
        else:
            return_low, return_high, return_sum = cross_low, cross_high, cross_sum
            
    if return_type == tuple:
        return (return_low, return_high, return_sum)
    else:
        return {'low':return_low, 'high':return_high, 'sum':return_sum}

def find_maximum_subarray_brute_force(A):
    max_sum = -np.inf
    for i in range(len(A)):
        for j in range(i, len(A)):
            subarray = A[i:j+1]
            sub_sum = np.sum(subarray)
            if sub_sum > max_sum:
                max_i = i
                max_j = j
                max_sum = sub_sum
    return (max_i, max_j, max_sum)

def find_maximum_subarray_kadane(A):
    max_ending_here = A[0]
    startOld = start = end = max_so_far = 0
    for i, x in enumerate(A[1:], 1):
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
        if max_ending_here < 0:
            start = i + 1
        elif max_ending_here == max_so_far:
            startOld = start
            end = i
    return (startOld, end, max_so_far)

def evaluate_correctness(A):
    return find_maximum_subarray(A, return_type=tuple) == find_maximum_subarray_brute_force(A)   