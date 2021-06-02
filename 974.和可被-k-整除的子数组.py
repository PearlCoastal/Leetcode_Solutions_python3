#
# @lc app=leetcode.cn id=974 lang=python3
#
# [974] 和可被 K 整除的子数组
#

# @lc code=start
from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        dic = defaultdict(int)
        pre, ans = 0, 0

        for i in A:
            pre += i

            if dic[pre % k] in dic:
                
            

# @lc code=end

A = [4,5,0,-2,-3,1]
K = 5

ob = Solution()
ans = ob.subarraysDivByK(A, K)
ans
