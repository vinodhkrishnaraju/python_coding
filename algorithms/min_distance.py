
from sys import maxsize
def threeSumClosest(A, B):
        
    
    A = list(set(A))
    A = sorted(A)
    print(A)
    n = len(A)
    result = [maxsize]
    distance = abs(sum(result) - B)
    # print(distance)
    for i in range(n-3):
        # print(abs(sum(A[i:i+3] - B)))
        if abs(sum(A[i:i+3]) - B) < distance:
            # print('Enters loop')
            result = A[i:i+3]
            distance = abs(sum(result) - B)

    # print(distance)
    # print(result)
    print(sum(result))


input = [ -5, 1, 4, -7, 10, -7, 0, 7, 3, 0, -2, -5, -3, -6, 4, -7, -8, 0, 4, 9, 4, 1, -8, -6, -6, 0, -9, 5, 3, -9, -5, -9, 6, 3, 8, -10, 1, -2, 2, 1, -9, 2, -3, 9, 9, -10, 0, -9, -2, 7, 0, -4, -3, 1, 6, -3 ]

input = [ -10, -10, -10 ]

input = [ -5, 1, 4, -7, 10, -7, 0, 7, 3, 0, -2, -5, -3, -6, 4, -7, -8, 0, 4, 9, 4, 1, -8, -6, -6, 0, -9, 5, 3, -9, -5, -9, 6, 3, 8, -10, 1, -2, 2, 1, -9, 2, -3, 9, 9, -10, 0, -9, -2, 7, 0, -4, -3, 1, 6, -3 ]
threeSumClosest(input, -1)