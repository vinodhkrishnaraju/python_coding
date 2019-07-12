def kthsmallest(self, A, B):
    k = B
    count = 0
    start = min(A)
    end = max(A)

    # find min and max values
    # find mid value
    # count values lesser or equal to mid
    # if count > k then change end value to mid -1
    # if count < k then change start value

    while True:
        mid = (start+end)//2
        count_smaller = 0
        count_smaller_equal = 0
        for num in A:
            if num < mid:
                count_smaller += 1
            if num <= mid:
                count_smaller_equal += 1
        
        if count_smaller_equal >=k and count_smaller < k:
            return mid
        
        elif count_smaller >= k:
            end = mid - 1
        
        else:
            start = mid + 1




class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        min_array = [None] * B
        
        for i in range(len(min_array)):
            min_array[i] = A[i]
        
        min_array = sorted(min_array)
            
        
        for i in range(B, len(A)):
            if A[i] < max(min_array):
                min_array.pop()
                min_array.append(A[i])
                min_array = sorted(min_array)
            
        return max(min_array)
                
                
        
        
        
