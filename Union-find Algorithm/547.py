class UnionFind:
    def __init__(self, M):
        self.parent = {}
        self.size = {}
        self.count = 0

        for i in range(M):
            self.parent[i] = i
            self.size[i] = 1
            self.count += 1

    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x
        
    def union(self, p, q):
        
        p_root = self.find(p)
        q_root = self.find(q)
        if q_root == p_root:
            return 
        self.parent[p_root] = q_root
        self.size[q_root] += self.size[p_root]
        self.count -= 1

    


class Solution:
    def findCircleNum(self, isConnected: [[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    uf.union(i, j)
        ans = 0
        ans = sorted(uf.size.items(), key = lambda x: x[1], reverse = True)
        
        
        return ans[0][1]

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
isConnected = [[1,1,1],[1,1,1],[1,1,1]]
ob = Solution()
ans = ob.findCircleNum(isConnected)
ans