#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#
'''
        slow, fast = 0, 1
        length = len(nums)

        for i in range(length-1):
            for j in range(i + 1, length):

                if nums[i] == nums[j]:
                    return nums[j]
        '''
        
# @lc code=start
class Solution:
    def findDuplicate(self, nums: [int]) -> int:

        slow, fast = 0, 0

        slow = nums[slow]
        fast = nums[nums[fast]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return fast
        
        
# @lc code=end
# nums = [3,1,3,4,2]
nums = [1,3,4,2,2]
ob = Solution()
ans = ob.findDuplicate(nums)
ans
