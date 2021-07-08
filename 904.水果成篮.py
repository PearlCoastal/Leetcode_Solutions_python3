#
# @lc app=leetcode.cn id=904 lang=python3
#
# [904] 水果成篮
#
import collections
# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        def atMostK(fruits: List[int], k: int):
            ans = 0
            win = collections.defaultdict(int)
            left, right = 0, 0

            for right in range(len(fruits)):
                if win[fruits[right]] == 0:
                    k -= 1
                win[fruits[right]] += 1
                while k < 0:
                    win[fruits[left]] -= 1
                    if win[fruits[left]] == 0:
                        k += 1
                    left += 1
                ans = max(ans, right - left + 1)
            return ans
        
        res = atMostK(fruits, 2)
        return res
# @lc code=end

tree = [3,3,3,1,2,1,1,2,3,3,4]

ob = Solution()
ans = ob.totalFruit(tree)
ans
