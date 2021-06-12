#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: [int], target: int) -> int:

        left, right = 0, len(nums)
        
        while left <= right:
            mid = int((left + right) / 2)

            if nums[mid] == target:
                return mid

            #mid左边为有序数组
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1
                    
# @lc code=end

nums = [4,5,6,7,0,1,2]
target = 0

ob = Solution()
ans = ob.search(nums, target)
ans