#
# @lc app=leetcode.cn id=646 lang=python3
#
# [646] 最长数对链
#

# @lc code=start
class Solution:
    def findLongestChain(self, pairs: [[int]]) -> int:

        pairs.sort(key = lambda x: x[0])
        dp = [1] * len(pairs)
        for i in range(len(pairs)):
            for j in range(i - 1, -1, -1):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

# @lc code=end

pairs = [[1,2], [2,3], [3,4]]

ob = Solution()
ans = ob.findLongestChain(pairs)
ans