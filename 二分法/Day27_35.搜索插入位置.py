#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        if nums[0] > target:
            return 0
        
        left, right = 0, len(nums) - 1
        while left <= right:
            
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
            
        return left
# @lc code=end

nums = [1,3,5,6]
target = 7

ob = Solution()
ans = ob.searchInsert(nums, target)
ans