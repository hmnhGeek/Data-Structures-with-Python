def leftrotation(l, k):
    if k < len(l):
        l1 = l[k::]
        l2 = l[0:k:1]
        return l1+l2
    else:
        k = k%len(l)
        return leftrotation(l, k)

def representatives(l):
    '''https://www.geeksforgeeks.org/rearrange-array-arri/'''
    '''Given an array of elements of length N, ranging from 0 to N – 1. All elements may not be present in the array. If element is not present then there will be -1 present in the array. Rearrange the array such that A[i] = i and if i is not present, display -1 at that place.'''
    maximum = max(l)
    L = [-1 for i in range(0, maximum+1)]

    for i in range(len(l)):
        if l[i] != -1:
            L[l[i]] = l[i]
    return L

def moveZeros(l):
    '''
        https://www.geeksforgeeks.org/move-zeroes-end-array-set-2-using-single-traversal/
    '''
    L = []

    for i in range(len(l)):
        if l[i] == 0:
            L.append(0)

    while 0 in l:
        l.remove(0)
    
    return l+L

def minSwaps(l, k):
    '''
        https://www.geeksforgeeks.org/minimum-swaps-required-bring-elements-less-equal-k-together/
    '''
    count = 0
    swaps = 0
    
    for i in l:
        if i <= k:
            count += 1

    for i in range(0, count):
        if l[i] > k:
            swaps += 1
    return swaps

def bubble_sort(l):
    passes = 0
    while True:
        swaps = False
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                temp = l[i+1]
                l[i+1]=l[i]
                l[i] = temp
                swaps = True
        passes += 1
        if swaps:
            continue
        else:
            break
    return l, passes

def kadane_algo(l):
    '''https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/'''

    max_so_far, max_ending_here = 0, 0

    for i in l:
        max_ending_here += i
        if max_ending_here < 0:
            max_ending_here = 0
        else:
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
    return max_so_far

def most_max(l, k):
    '''https://www.geeksforgeeks.org/find-k-numbers-occurrences-given-array/'''
    done = {}

    for i in l:
        if i not in done:
            done.update({i:0})
            for j in l:
                if j == i:
                    done[i] += 1
    res = []
    
    for i in done:
        if done[i] == k:
            res.append(i)
    res.sort(reverse=True)
    return done
            
                
