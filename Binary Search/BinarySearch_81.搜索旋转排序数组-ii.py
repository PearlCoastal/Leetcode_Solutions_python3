#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start
class Solution:
    def search(self, nums: [int], target: int) -> bool:

        left, right = 0, len(nums) - 1
        
        while left <= right:

            mid = int((left + right) / 2)
            if nums[mid] == target:
                return True
            
            #处理重复元素
            while left < mid and nums[left] == nums[mid]:
                left += 1
            
            #左边为有序部分
            if nums[left] <= nums[mid]:
                #判断target在哪一部分
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
            
                else:
                    left = mid + 1
            #右边为有序部分
            else:
                #判断target在哪一部分
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False
            

            
        
# @lc code=end

nums = [6,7,8,1,2,3,4,5]
target = 4

ob = Solution()
ans = ob.search(nums, target)
ans