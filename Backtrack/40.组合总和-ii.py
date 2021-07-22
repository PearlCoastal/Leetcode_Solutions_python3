#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        
        length = len(candidates)
        if not length: return []

        candidates.sort()
        ans = []
        path = []
        self.find_path(candidates, target, 0, length, path, ans)
        return ans

    def find_path(self, candidates: [int], target: int, begin: int, length: int, path: [int], ans: [int]):
        
        if target == 0 and path not in ans:
            ans.append(path.copy())

        else:
            for i in range(begin, length):
                if i > begin and candidates[i] == candidates[i - 1]:
                    continue

                left_num = target - candidates[i]

                if left_num < 0:
                    break

                path.append(candidates[i])
                self.find_path(candidates, left_num, i + 1, length, path, ans)
                
                path.pop()

# @lc code=end
candidates = [10,1,2,7,6,1,5]
target = 8


ob = Solution()
ans = ob.combinationSum2(candidates, target)
ans
