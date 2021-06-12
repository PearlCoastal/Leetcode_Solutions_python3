
class Solution:
    def findSubstring(self, s: str, words:[str]) -> [int]:
        n = len(words)
        size = len(words[0])
        words = sorted(words)
        ans = []

        def helper(substring):
            cur = []
            for i in range(0, len(substring), size):
                cur.append(substring[i : i+size])
            cur = sorted(cur)
            return cur == words
        
        for i in range(len(s) - n * size + 1):
            if helper(s[i : i + n * size]):
                ans.append(i)
        
        return ans

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]

ob = Solution()
ans = ob.findSubstring(s, words)
ans