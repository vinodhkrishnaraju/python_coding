from pdb import set_trace as bp
def searchRange(A, B):
    
    # set start and end
    # get mid point
    # if mid == target:
    #   check forward and backward till it matches
    # if mid > target:
    #   end = mid - 1
    # if mid < target:
    #   start = mid + 1
    
    if len(A) <= 1:
        return A
    start = 0
    end = len(A) - 1
    # print(len(A))
    result = []
    while start <= end:
        mid = (start+end) // 2
        if A[mid] == B:
            result.append(mid)
            i = mid -1
            while A[i] == B:
                i -= 1
            result.append(i+1)
            j = mid + 1
            while A[j] == B and j < end:
                # result.append(j)
                j += 1
            result.append(j)
            return result
        elif A[mid] > B:
            end = mid - 1  
        elif A[mid] < B:
            start = mid + 1
            
    return result
    # print(min(result))
    # print(max(result))

A = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ]
B = 10

result = searchRange(A, B)
print(min(result))
print(max(result))



