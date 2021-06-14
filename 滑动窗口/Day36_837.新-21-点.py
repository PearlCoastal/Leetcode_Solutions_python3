#
# @lc app=leetcode.cn id=837 lang=python3
#
# [837] 新21点
#

# @lc code=start
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [0] * (K + W)
        window_sum = 0
        for i in range(K, K + W):
            if i <= N:
                dp[i] = 1
                window_sum += dp[i]

        for i in range(K - 1, -1, -1):
            dp[i] = window_sum / W
            window_sum += dp[i] - dp[i + W]

        return dp[0]
# @lc code=end

N = 21
K = 17
W = 10

ob = Solution()
ans = ob.new21Game(N, K, W)
ans
