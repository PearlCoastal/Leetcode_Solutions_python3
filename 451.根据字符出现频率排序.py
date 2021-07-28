#
# @lc app=leetcode.cn id=451 lang=python3
#
# [451] 根据字符出现频率排序
#

# @lc code=start
import collections
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        dic = collections.defaultdict(int)
        character = list(s)
        for char in character: 
            dic[char] += 1
        heap = []
        for char in dic:
            heapq.heappush(heap, (-dic[char], char))
        ans = []
        while heap:
            freq, char = heapq.heappop(heap)
            ans.append(char * (-freq))
        return "".join(ans[i] for i in range(len(ans)))
# @lc code=end
s = "Aabb"

ob = Solution()
ans = ob.frequencySort(s)
ans
