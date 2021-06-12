#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        ans = []
        dic = defaultdict(int)
        for i in range(len(nums)):
            dic[nums[i]] += 1
        
        sort_dic = sorted(dic.items(), key = lambda item: item[1], reverse = True)
        
        for i in range(k):
            ans.append(sort_dic[i][0])
            
        return ans

        # @lc code=end

nums = [1,1,1,2,2,3]
k = 2

ob = Solution()
ans = ob.topKFrequent(nums, k)
ans

