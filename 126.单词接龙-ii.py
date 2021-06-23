#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#
import collections
# @lc code=start
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: [str]) -> [[str]]:
        cost = collections.defaultdict(lambda: float("inf"))
        cost[beginWord] = 0
        neighbors = collections.defaultdict(list)
        ans = []

        for word in wordList:
            for i in range(len(word)):
                neighbors[word[:i] + "*" + word[i + 1 :]].append(word)
        q = collections.deque([[beginWord]])

        while q:
            path = q.popleft()
            cur = path[-1]
            if cur == endWord:
                ans.append(path.copy())
            else:
                for i in range(len(cur)):
                    for neighbor in neighbors[cur[:i] + "*" + cur[i + 1 :]]:
                        if cost[cur] + 1 <= cost[neighbor]:
                            q.append(path + [neighbor])
                            cost[neighbor] = cost[cur] + 1
        return ans
# @lc code=end

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

ob = Solution()
ans = ob.findLadders(beginWord, endWord, wordList)
ans