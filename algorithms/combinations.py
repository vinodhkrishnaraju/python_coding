def combinations(A, k = None):
    n = len(A)
    result = [ [] ]
    if n == 0:
        return result

    for i in A:
        # result.extend( [ x + [i] for x in result] )
        temp = []
        for x in result:
            temp.append( [i] + x )
        result.extend(temp)
    return result



print(combinations([1,2,3,4],2))




def combinek(arr, k):
    if len(arr) <= k:
        yield arr
        arr = []  


    if arr:
        head = arr[0]
        rest = arr[1:]
        for c in combinek(rest, k - 1):
            yield [head] + c
        for c in combinek(rest, k):
            yield c


for i in range(4):
    print(list(combinek(['b','c','d'],i)))
print('------------')


a = combinations([1,2,3,4])
# print(a)
b = filter(lambda x: len(x) == 2, a)
print(list(b))

def combinationSum(A, B):
        
    result = [[]]
    n = len(A)
    
    if n == 0:
        return result
        
    for i in A:
        result.extend( [ [i] + x for x in result  ]   )
    
    # result

    return list(filter(lambda x: sum(x) == B, result ) )


# print(combinationSum([1,2,3,4], 7) )

def permute(A):
    
    
    result = []
    n = len(A)
    if n == 1:
        return [A]
    
    for i in range(len(A)):
        string = A[i]
        temp = A[:i] + A[i+1:]
        result.extend( [ [string] + x for x in permute(temp)  ]  )
    
    return result



print(combinations([1,2,3,4]))
