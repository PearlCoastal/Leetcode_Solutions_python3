
class Solution:
    def permute(self, nums: [int]) -> [[int]]:

        res = []

        def backtrack(nums, path):

            if not nums:
                res.append(path)
                return res

            for i in range(len(nums)):

                backtrack(nums[:i] + nums[i+1:], path + [nums[i]])

        backtrack(nums, [])
        return res

nums = [1,2,3]
ob = Solution()

ans = ob.permute(nums)
ans

'''
1.  list[i:j]
    i......j-1
'''