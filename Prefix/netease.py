import collections
class Solution:
    def f(self, scores, m):
        n = len(scores)
        arr = [0] * 151
        ans = []
        # 离散化，统计分数为 i 的有多少人
        for i in range(n):
            arr[scores[i]] += 1
        # 构造前缀和
        for i in range(1, len(arr)):
            arr[i] = arr[i] + arr[i - 1]
        # 模拟 m 次询问
        for i in range(len(m)):
            score = scores[m[i] - 1]
            sum = arr[score]
            ans.append(sum / n * 100)
        return ans

scores = [50, 60, 70]
m = [1, 2]

ob = Solution()
ans = ob.f(scores, m)
ans