import collections
class Solution:
    
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        dic = collections.Counter(nums)
        dic = list(dic.items())
        self.k = k
        self.h = [(0, 0)]

        for i in range(len(dic)):
            if len(self.h) < self.k + 1:
                self.heappush(dic[i])
            else:
                if dic[i][1] > self.h[1][1]:
                    self.heappop()
                    self.heappush(dic[i])
        
        return [x[0] for x in self.h[1:]]

    def heappush(self, a):
        self.h.append(a)
        self.shift_up(len(self.h) - 1)

    def heappop(self):
        if len(self.h) == 1:
            return None
        self.h[1] = self.h[(len(self.h) - 1)]
        self.h.pop()
        self.shift_down(1)
        #return pop_node

    def shift_up(self, i):
        while i // 2 > 0:
            if self.h[i][1] < self.h[i//2][1]:
                self.h[i], self.h[i//2] = self.h[i//2], self.h[i]
            i = i // 2

    def shift_down(self, i):
        while (i * 2) < self.k:
            min_child = self.minChild(i)
            if self.h[i][1] > self.h[min_child][1]:
                self.h[i], self.h[min_child] = self.h[min_child], self.h[i]
            i = min_child
        
    def minChild(self, i):
        left_child = i * 2
        right_child = i * 2 + 1
        if right_child > len(self.h) - 1:
            return left_child
        if self.h[left_child][1] < self.h[right_child][1]:
            return left_child
        else:
            return right_child
'''
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:

        dic = Counter(nums)
        h = []
        for num, freq in dic.items():
            if len(h) < k:
                heapq.heappush(h, (freq, num))
            else:
                if freq > h[0][0]:
                    heapq.heappop(h)
                    heapq.heappush(h, (freq, num))
        return [x[1] for x in h]
'''    
nums =  [5,-3,9,1,7,7,9,10,2,2,10,10,3,-1,3,7,-9,-1,3,3]
k = 3

ob = Solution()
ans = ob.topKFrequent(nums, k)
ans

    