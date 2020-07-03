# Uses python3
import sys
import random

def partition3(A, l, r):
    """
partition3: A partition for quicksort algorithm. We'll use the 3-way to handle few equal elements in array (happens
a lot in practical use.)
This function is called from the main function quick_sort.
"""
    lt = l  # We initiate lt to be the part that is less than the pivot
    i = l   # We scan the array from left to right
    gt = r  # The part that is greater than the pivot
    pivot = A[l]    # The pivot, chosen to be the first element of the array, that why we'll randomize the first elements position
                    # in the quick_sort function.
    while i <= gt:      # Starting from the first element.
        if A[i] < pivot:
            A[lt], A[i] = A[i], A[lt]
            lt += 1
            i += 1
        elif A[i] > pivot:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        else:
            i += 1
            
    return lt, gt
    
def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r: 
        return
    k = random.randint(l, r)
    a[k], a[l] = a[l], a[k]
    lt, gt = partition3(a, l, r)
    randomized_quick_sort(a, l, lt - 1)
    randomized_quick_sort(a, gt + 1, r)  

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
