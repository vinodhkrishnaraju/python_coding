# def perm(a, k=0):
#    if k == len(a):
#       print(a)
#    else:
#       for i in range(k, len(a)):
#          a[k], a[i] = a[i] ,a[k]
#          perm(a, k+1)
#          a[k], a[i] = a[i], a[k]

# print(perm([1,2,3], k=3))


# def permutList(l):
#     if not l:
#         return [[]]
#     res = []
#     for e in l:
#         temp = l[:]
#         temp.remove(e)
#         res.extend([[e] + r for r in permutList(temp)])

#     return res

# print(permutList([1,2,3]))

# import itertools

# print(list(itertools.permutations([1,2,3])))

def perm2(A, k):
    r = [[]]
    for i in range(len(A)):
        r = [[a] + b for a in A for b in r if a not in b]
    return r

print(perm2([1,2,3],3))



class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        res=[]
        nums.sort()
        self.permute(nums,[],res)
        return res
 
    def permute(self,nums,tmplist,res):
        if len(nums)==0:
            res.append(tmplist)
            return
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            self.permute(nums[:i]+nums[i+1:],tmplist+[nums[i]],res)





