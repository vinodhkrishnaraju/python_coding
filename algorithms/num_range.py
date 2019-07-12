class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def numRange(self, A, B, C):
        
        result_set = []
        for i in range(len(A)):
            for j in range(i+1, len(A) +1):
                # print(A[i:j])
                if sum(A[i:j]) in range(B,C+1):
                    result_set.append(A[i:j])
        
        return len(result_set)


A = [ 61, 71, 69, 97, 40, 6, 57, 70, 13, 70, 21, 46, 21, 71, 49, 83, 84, 71, 97, 13, 80, 50 ]
B = 58
C = 942
print(Solution().numRange(A, B, C))