#
# @lc app=leetcode.cn id=464 lang=python3
#
# [464] 我能赢吗
#

# @lc code=start
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        def dfs(acc):
            if acc >= desiredTotal:
                return False
            for n in range(1, maxChoosableInteger + 1):
                # 对方有一种情况赢不了，我就选这个数字就能赢了，返回 true，代表可以赢。
                if not dfs(acc + n):
                    return True
            return False

    # 初始化集合，用于保存当前已经选择过的数。
        return dfs(0)
# @lc code=end

maxChoosableInteger = 10
desiredTotal = 11

ob = Solution()
ans = ob.canIWin(maxChoosableInteger, desiredTotal)
ans