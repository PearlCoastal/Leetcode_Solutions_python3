
class Solution:
    def minNumber(self, nums: [int]) -> str:
        self.heap = [0]
        nums = [str(num) for num in nums]
        for num in nums:
            self.heappush(num)
        
        ans = []
        while len(self.heap) - 1 >= 1:
            ans.append(self.heappop())
        return ''.join(ans)
    
    def heappush(self, num):
        self.heap.append(num)
        self.shift_up(len(self.heap) - 1)
    def shift_up(self, i):
        while i // 2 > 0:
            if self.heap[i // 2] + self.heap[i] >= self.heap[i] + self.heap[i // 2]:
                self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]
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
            if self.heap[i] + self.heap[min_child] >= self.heap[min_child] + self.heap[i]:
                self.heap[i], self.heap[min_child] = self.heap[min_child], self.heap[i]
            i = min_child
    def minChild(self, i):
        left_child = i * 2
        right_child = i * 2 + 1
        if right_child > len(self.heap) - 1:
            return left_child
        if self.heap[left_child] + self.heap[right_child] < self.heap[right_child] + self.heap[left_child]:
            return left_child
        else:
            return right_child


nums = [824,9609,4398,8247]

ob = Solution()
ans = ob.minNumber(nums)
ans