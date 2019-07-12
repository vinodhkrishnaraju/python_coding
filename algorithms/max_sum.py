class Solution:
    # @param A : tuple of integers
    # @return an integer

    def get_subsets(self, A):

        result = [[]]

        for i in A:
            result.extend([subset + [i] for subset in result])

        return result

    def maxSubArray(self, A):

        # print(self.get_subsets(A))
        L = A
        print([L[i:i+j] for i in range(0,len(L)) for j in range(1,len(L)-i+1)])

        [A[i:i+j] for i in range(0, len(A)) for j in range(i, len(A) -i + 1 )]

        
        # sliding_window = range(1,len(A))
        
        # max
        # result_tuple = None
        
        # for start in sliding_window:
        #     sum_vec = [sum(A[i:(i+start)]) for i in range(len(A) - start) ]
        #     max_val = sum_vec[0] 
        #     index_val = 0
            
        #     for index in range(len(sum_vec)):
        #         if(max_val < sum_vec[index]):
        #             max_val = sum_vec[index]
        #             index_val = index
        #     if result_tuple is None:
        #         result_tuple = (max_val,A[index:(index+start)])
        #     elif(result_tuple[0] > max_val):
        #         result_tuple = (max_val,A[index:(index+start)])
        # return list(result_tuple[1])
                
print(Solution().maxSubArray([1,2,5]))