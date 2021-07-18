class Union_Find:

    def __init__(self, M):
        self.parent = {}
        self.size = {}
        self.count = 0

        for i in range(M):
            self.parent[i] = i
            self.size[i] = 1
            self.count = 1
        
    def find(self, x):
        if x != self.find(x):
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        return x
    
    def union(self, p, q):
        if self.connected(p, q):
            return 
        leader_p = self.find(p)
        leader_q = self.find(q)

        if self.size(leader_p) < self.size(leader_q):
            self.parent[leader_p] = leader_q
            self.size[leader_q] += self.size[leader_p]
        else:
            self.parent[leader_q] = leader_p
            self.size[leader_p] = self.size[leader_q]
        self.count -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)
