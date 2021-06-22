题目：
====

(https://binarysearch.com/problems/Shortest-Cycle-Containing-Target-Node)

思路：
====

求最短距离，找BFS

- BFS：记录最短的环，根据BFS的特性，在遇到环的时候，就一定是最短的。

- 使用集合visited()记录已经访问过的节点，遇到新节点是，检查visited()是否已经访问过。

- 题目要求返回 包含target的最短的环。与其从图的起点开始，不如直接从target开始，这样只要找到了环，就一定包含target。

代码：
====

```python
class Solution:
    def solve(self, graph, target):
        q = collections.deque([target])
        visited = set()
        steps = 0
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                visited.add(cur)
                for neighbor in graph[cur]:
                    if neighbor not in visited:
                        q.append(neighbor)
                    elif neighbor == target:
                        return steps + 1
            steps += 1
        return -1

```

复杂度分析：
====
V 是节点数，E 是边数
- 时间复杂度：O(V + E)
- 空间复杂度：O(V)