#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        length = len(candidates)
        if not length: return []

        path = []
        ans = []
        self.backtrack(candidates, target, 0, length, path, ans)

    def backtrack(self, candidates: [int], target: int, begin: int, length: int, path: [int], ans: [int]):

        if target == 0:
            ans.append(path.copy())
        
        for i in range(begin, length):
            left_num = target - candidates[i]

            if left_num < 0:
                break

            else:
                path.append(candidates[i])
                self.backtrack(candidates, left_num, i, length, path, ans)
            
            path.pop()

# @lc code=end

candidates = [2,3,5]
target = 8

ob = Solution()
ans = ob.combinationSum(candidates, target)
ans