#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: [int]) -> [[int]]:

        nums.sort()
        ans = []
        path = []
        visited = [0 for i in range(len(nums))]

        def backtrack(index, path):
            ans.append(path)

            for i in range(index, len(nums)):
                
                if i > index and nums[i] == nums[i - 1]:
                    continue
        
                # path.append(nums[i])
                backtrack(i + 1, path + [nums[i]])

        backtrack(0, [])
        return ans
# @lc code=end

nums = [1,2,2]
ob = Solution()
ans = ob.subsetsWithDup(nums)
ans