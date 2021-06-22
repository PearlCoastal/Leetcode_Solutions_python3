import collections

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

