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

def find_maximum_subarray(A, low=None, high=None):
    '''p72 Introduction To Algorithms'''
    if low == None:
        low = 1 # low is 1 because A[0] is NaN
    if high == None:
        high = len(A) - 1
    
    if high == low:
        return (low, high, A[low])
    else:
        mid = int(np.floor((low + high) / 2))
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = _find_max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)