class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):
        
        xor = 0
        pairs = ((i, j) for i in A for j in A)
        for i, j in pairs:
            i = int(format(i, 'b'))
            j = int(format(j, 'b'))
            summ = sum(list(map(int, str(i^j))))
            xor += summ
            print(xor)
        
        return xor

    def isPower(self, A):
        
        # x is base integer
        # y is power
        
        # increment base
        for x in range(2, A):
            print(x)
            y = 1
            # increment power
            while y < A:
                print('\t', y)
                y +=1
                if (x ** y) == A:
                    return 0
            
        return 1

# print(Solution().hammingDistance([ 96, 96, 7, 81, 2, 13 ]))
print(Solution().isPower(4))