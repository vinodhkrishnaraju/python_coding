class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        nums = A
        numhash={}
        for i in range(len(nums)):
            numhash[nums[i]]=1
        result=1
        for i in range(len(nums)):
            if nums[i] in numhash:
                k=1
                counter=1
                while nums[i]-k in numhash:
                    counter+=1
                    del numhash[nums[i]-k]
                    k+=1
                k=1
                while nums[i]+k in numhash:
                    counter+=1
                    del numhash[nums[i]+k]
                    k+=1
                result=max(result,counter)
        return result
                
