#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        
        if not candidates:
            return []
        ans = []
        path = []

        def backtrack(index: int, path: [int], target: int):

            if target == 0:
                ans.append(path.copy())
            for i in range(index, len(candidates)):
                left = target - candidates[i]
                if left < 0:
                    break
                else:
                    path.append(candidates[i])
                    backtrack(i, path, left)
                path.pop()
        backtrack(0, [], target)
        return ans
          

# @lc code=end

candidates = [2,3,5]
target = 8

ob = Solution()
ans = ob.combinationSum(candidates, target)
ans