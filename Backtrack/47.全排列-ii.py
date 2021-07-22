#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: [int]) -> [[int]]:
        nums.sort()
        ans = []
        path = []
        check = [0 for i in range(len(nums))]

        def backtrack(nums, path, check):
            if len(path) == len(nums):
                ans.append(path.copy())

            for i in range(len(nums)):
                if check[i] == 1:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 1:
                    continue 
                
                check[i] = 1
                backtrack(nums, path + [nums[i]], check)
                check[i] = 0
        backtrack(nums, [], check)
        return ans
# @lc code=end

nums = [1,1,2]

ob = Solution()
ans = ob.permuteUnique(nums)
ans