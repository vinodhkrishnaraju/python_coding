from pdb import set_trace as bp


def quick_sort(A):
    _quick_sort(A, 0, len(A)-1)

def _quick_sort(A, left, right):
    if left<right:
        pivot = A[(left+right) // 2]
        index = partition(A, left, right, pivot)
        _quick_sort(A, left, index-1)
        _quick_sort(A, index, right)

    # inplace sort so no need to return A

def partition(A, left, right, pivot):

    while left <= right:
        while A[left] < pivot:
            left += 1
        while A[right] > pivot:
            right -= 1


        if left <= right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1

    return left


A = [4,6,2,50,170,8,29,1]
A = [8,7,1,2,6,9,10,2,11]
A = [2,7,1,2,6,9,10,8,11]
quick_sort(A)
print(A)


"""
1. Find pivot element. Say middle
2. Implement partition and find index
    move and swap left and right
    At crossing return left as index
3. Repeat for left half and right half
"""








