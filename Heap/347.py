import collections
class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:

        dic = collections.Counter(nums)
        dic = list(dic.items())
        self.k = k
        self.heap = [(0, 0)] 

        for i in range(len(dic) - 1):
            if len(self.heap) < self.k + 1:
                self.heappush(dic[i])
            else:
                if dic[i][1] > self.heap[1][1]:
                    self.heappop()
                    self.heappush(dic[i])
        return (x[0] for x in self.heap[1: ])

    def heappush(self, a):
        self.heap.append(a)
        self.shift_up(len(self.heap)- 1)
    def shift_up(self, i):
        node = self.heap
        while i // 2 > 0:
            if self.heap[i][1] < self.heap[i // 2][1]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2
    def heappop(self):
        if len(self.heap) == 1:
            return None
        self.heap[1] = self.heap[len(self.heap) - 1]
        self.heap.pop()
        self.shift_down(1)

    def shift_down(self, i):
        while i * 2 < self.k:
            min_child = self.minChild(i)
            if self.heap[i][1] > self.heap[min_child][1]:
                self.heap[i], self.heap[min_child] = self.heap[min_child], self.heap[i]
            i = min_child
    def minChild(self, i):
        if i * 2 + 1 > len(self.heap) - 1:
            return i * 2
        if self.heap[i * 2] < self.heap[i * 2 + 1]:
            return i * 2
        else:
            return i * 2 + 1

nums =  [5,-3,9,1,7,7,9,10,2,2,10,10,3,-1,3,7,-9,-1,3,3]
k = 3

ob = Solution()
ans = ob.topKFrequent(nums, k)
ans

  