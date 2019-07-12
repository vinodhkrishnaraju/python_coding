def merge_sort(A):

    n = len(A)

    if n == 1:
        return A

    mid = n // 2

    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])

    i,j,k=0,0,0

    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1 
    if i < len(left):
        A[k] = left[i]
        k += 1
    else:
        A[k] = right[j]
        k += 1

    print(A)
    return A

print(merge_sort([4,6,2,50,170,8,29,1]))


