#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
import collections
# @lc code=startclass Solution:
class Solution:
    def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
        q = collections.deque() 
        ans = []

        for i in range(len(nums)):

            while q and nums[q[-1]] <= nums[i]: 
                q.pop() 
                
            while q and i - q[0] >= k: 
                q.popleft() 

            q.append(i)

            if i >= k - 1: ans.append(nums[q[0]])
        return ans
# @lc code=end

nums = [1,3,-1,-3,5,3,6,7]
k = 3

# nums = [1]
# k = 1

# nums = [1,-1]
# k = 1

# # nums = [9,11]
# # k = 2

# # nums = [4,-2]
# # k = 2

ob = Solution()
ans = ob.maxSlidingWindow(nums, k)
ans