class Solution:
    # @param A : integer
    # @return an integer
    def get_factorial(self, A):
        factorial = 1
        for i in range(1, A+1):
            factorial *= i
        return factorial
        
    def trailingZeroes(self, A):
        
        factorial = self.get_factorial(A)
        print(factorial)
        trailing_zeros = 0
        for item in str(factorial)[::-1]:
            if int(item) == 0:
                trailing_zeros += 1
            else:
                return trailing_zeros

print(Solution().trailingZeroes(9247))