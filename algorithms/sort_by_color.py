def sortColors(A):
    
    color_hash = {}
    for i in A:
        if i in color_hash.keys():
            color_hash[i] = color_hash[i] + 1
        else:
            color_hash[i] = 1
    
    order = sorted(list(color_hash.keys()))
    i = 0
    dummy_array = []
    for color in order:
        v = color_hash[color]
        dummy_array.extend([color] * v)

    for i in range(len(A)):
        A[i] = dummy_array[i]


A = [ 2, 0, 0, 1, 0, 0, 2, 2, 1, 1, 0, 0, 1, 0, 2, 1, 1, 0, 1, 0, 1, 2, 2, 2, 0, 0, 1, 0, 2, 1, 1, 2, 1, 2, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 0, 1, 0, 2, 1, 2, 0, 2, 0, 1, 1, 0, 2, 2, 1, 2, 0, 2, 1, 1, 1, 2, 0, 1, 0, 2, 2, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 2, 1, 1, 0, 2, 1, 2, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 1, 1, 0, 2, 1, 2, 2, 2, 1, 2, 2, 0, 1, 0, 1, 2, 1, 1, 0, 1, 2, 0, 1, 0, 2, 2, 1, 2, 1, 0, 2, 2, 1, 1, 0, 2, 1, 2 ]

A = [0]
sortColors(A)
print(A)