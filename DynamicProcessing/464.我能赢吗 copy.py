#
# @lc app=leetcode.cn id=464 lang=python3
#
# [464] 我能赢吗
#

# @lc code=start
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        visited = {}

        def dfs(choices, rest):
            key = tuple(choices)
            if key in visited:
                return visited[key]
            
            if choices[-1] >= rest:
                visited[key] = True
                return visited[key]
            
            for i in range(len(choices)):
                if not dfs(choices[:i] + choices[i+1:], rest - choices[i]):
                    visited[key] = True
                    return visited[key]
            
            visited[key] = False
            return visited[key]
        
        choices = [i for i in range(1, maxChoosableInteger + 1)]
        if sum(choices) < desiredTotal:
            return False

        return dfs(choices, desiredTotal)

# @lc code=end

maxChoosableInteger = 10
desiredTotal = 13

ob = Solution()
ans = ob.canIWin(maxChoosableInteger, desiredTotal)
ans
