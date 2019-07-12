class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        
        # 20 -> 7 and 13
        # Find all primes less than A
        # Combination is equal to A
        items = [i for i in range(2, A)]
        index = 0
        # for num in range(2, A):
        while index < len(items):
            # print(num)
            num = items[index]
            temp = num
            while num < A:
                num += temp
                if num in items:
                    items.remove(num)

            index += 1

        
        return items

    def is_prime(self, A):

        if A == 0 or A == 1:
            return False
        for x in range(2, A):
            if A%x == 0:
                return False
        return True

print(Solution().primesum(1048574))

# print(list(filter(Solution().is_prime, range(1,40))))

