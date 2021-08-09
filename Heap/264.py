class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        factors = [2, 3, 5]
        seen = {1}
        self.heap = [0]
        self.heappush(1)
        
        for i in range(n - 1):
            num = self.heappop()
            for factor in factors:
                element = num * factor
                if element not in seen:
                    seen.add(element)
                    self.heappush(element)
        return self.heappop()
    
    def heappush(self, num):
        self.heap.append(num)
        self.shift_up(len(self.heap) - 1)

    def shift_up(self, i):
        while i // 2 > 0:
            if self.heap[i // 2] > self.heap[i]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    def heappop(self):
        if len(self.heap) == 1:
            return None
        pop_node = self.heap[1]
        self.heap[1] = self.heap[len(self.heap) - 1]
        self.heap.pop()
        self.shift_down(1)
        return pop_node

    def shift_down(self, i):
        while i * 2 <= len(self.heap) - 1:
            min_child = self.minChild(i)
            if self.heap[i] > self.heap[min_child]:
                self.heap[i], self.heap[min_child] = self.heap[min_child], self.heap[i]
            i = min_child

    def min_child(self, i):
        left_child = i * 2
        right_child = i * 2 + 1
        if right_child > len(self.heap) - 1:
            return left_child
        if self.heap[right_child] > self.heap[left_child]:
            return left_child
        else:
            return right_child
            
n = 10

ob = Solution()
ans = ob.nthUglyNumber(n)
ans