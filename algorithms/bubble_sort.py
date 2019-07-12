def bubble_sort(A):
    n = len(A)

    for i in range(n):

        for j in range(i+1, n):

            if A[i] > A[j]:

                A[i], A[j] = A[j], A[i]
    return A

print(bubble_sort([4,6,2,50,170,8,29,1]))