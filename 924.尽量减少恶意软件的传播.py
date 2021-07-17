#
# @lc app=leetcode.cn id=924 lang=python3
#
# [924] 尽量减少恶意软件的传播
#

# @lc code=start
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}
    
    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x
    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        self.parent[p_root] = q_root
        self.size[q_root] += self.size[p_root]
    
class Solution:
    def minMalwareSpread(self, graph: [[int]], initial: [int]) -> int:
        uf = UnionFind()

        for i in range(len(graph)):
            for j in range(i, len(graph[0])):
                if graph[i][j] == 1:
                    uf.union(i, j)

        initial.sort()
        max_size, index, fi = 0, -1, []
        count = collections.defaultdict(int)

        for init in initial:
            fi.append(uf.find(init))
            count[fi[-1]] += 1
            
        for i in range(len(initial)):
            if count[fi[i]] > 1:
                continue
            if uf.size[fi[i]] > max_size:
                max_size = uf.size[fi[i]]
                index = initial[i]
        
        return index if index != -1 else initial[0]
        
# @lc code=end

