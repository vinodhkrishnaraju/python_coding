def binary_search(A, target):

    n = len(A)

    first = 0
    last = n - 1
    mid = n//2

    while first <= last:

        mid = (first+last) // 2
        if target == A[mid]:
            return True
        elif target>A[mid]:
            first = mid + 1
        else:
            last = mid - 1

    return False


print(binary_search([4,7,8,9,11,13,16,50], 16))
print(binary_search([4], 4))


