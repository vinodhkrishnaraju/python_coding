class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        temp = [None] * len(A)
        n = 5
        print(A)
        # divide to get new value
        # mod to get old value
        for i in range(len(A)):
            # A[i] += (A[A[i]]%n)*n
            A[i] += (A[A[i]]%n)*n
            
        print(A)
        for i in range(len(A)):
            A[i] = A[i]//n
        # A = temp
        print(A)

# 4 0 2 1 3 


print(Solution().arrange([ 4, 0, 2, 1, 3 ]))



# def perm(A):

#     if A == []:
#         return []
#     res = []
#     for i in A:
#         temp = A[:]
#         temp.remove(i)
#         res.extend([[i] + r in perm(temp)])



# 3   4   2   0   1