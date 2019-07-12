
swaps = 0

def merge_sort(A):

    """
    Return if len <= 1
    Get midpoint
    Split into left and right array
    Mergesort left
    Mergesort right

    modify array based on left and right output
    iterate pending items in left and right array

    """
    if len(A) <= 1:
        return


    mid = len(A)//2
    left = A[:mid]
    right = A[mid:]
    merge_sort(left)
    merge_sort(right)

    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):

        if left[i] > right[j]:
            A[k] = right[j]
            j += 1
        else:
            A[k] = left[i]
            i += 1
        k += 1

    # pending items in left and right

    while i < len(left):
        A[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        A[k] = right[j]
        j += 1
        k += 1


A = [8,2,5,4,3,7,1]
merge_sort(A)
print(A)






