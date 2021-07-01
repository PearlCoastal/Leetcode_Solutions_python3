#
# @lc app=leetcode.cn id=464 lang=python3
#
# [464] 我能赢吗
#

# @lc code=start
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= maxChoosableInteger:
            return True
        if sum(range(maxChoosableInteger + 1)) < desiredTotal:
            return False
        # picked 用于保存当前已经选择过的数。
        # acc 表示当前累计的数字和
        def backtrack(picked, acc):
            if acc >= desiredTotal:
                return False
            if len(picked) == maxChoosableInteger:
                # 说明全部都被选了，没得选了，返回 False， 代表输了。
                return False
            for n in range(1, maxChoosableInteger + 1):
                if n not in picked:
                    picked.add(n)
                    # 对方有一种情况赢不了，我就选这个数字就能赢了，返回 true，代表可以赢。
                    if not backtrack(picked, acc + n):
                        picked.remove(n)
                        return True
                    picked.remove(n)
            return False

        # 初始化集合，用于保存当前已经选择过的数。
        return backtrack(set(), 0)
# @lc code=end

maxChoosableInteger = 10
desiredTotal = 3

ob = Solution()
ans = ob.canIWin(maxChoosableInteger, desiredTotal)
ans
