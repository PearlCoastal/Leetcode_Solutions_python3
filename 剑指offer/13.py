import collections
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:

        def sumx(i):
            ans = 0
            while i > 0:
                ans += i % 10
                i //= 10
            return ans

        queue = collections.deque()
        queue.append((0, 0))
        visited = set()

        while queue:
            i, j = queue.popleft()
            if i < m and j < n and sumx(i) + sumx(j) <= k and (i, j) not in visited:
                queue.append((i + 1, j))
                queue.append((i, j + 1))
                visited.add((i, j))
        
        return len(visited)

m = 2
n = 3
k = 1

ob = Solution()
ans = ob.movingCount(m, n, k)
ans