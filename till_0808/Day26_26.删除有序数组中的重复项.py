#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: [int]) -> int:

        if not nums:
            return 0

        slow, fast = 0, 1
        
        while fast < len(nums):

            if nums[fast] == nums[slow]:
                nums.remove(nums[fast])

            else:
                slow = fast
            fast = slow + 1

        return len(nums)

# @lc code=end

# nums = [0,0,1,1,1,2,2,3,3,4]
# nums = [1,1,2]
nums = []

ob = Solution()
ans = ob.removeDuplicates(nums)
ans