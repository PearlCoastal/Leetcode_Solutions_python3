
class Solution:
    def lastStoneWeight(self, stones: [int]) -> int:

        self.heap = [0]
        for stone in stones:
            self.heappush(stone * (-1))
        while len(self.heap) > 2:
            x = -self.heappop()
            y = -self.heappop()
            if x != y:
                self.heappush(y - x)
        return -self.heap[1] if len(self.heap) > 1 else 0

    def heappush(self, num):
        self.heap.append(num)
        self.shift_up(len(self.heap) - 1)
    def shift_up(self, i):
        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:
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
    def minChild(self, i):
        left_child = i * 2
        right_child = i * 2 + 1
        if right_child > len(self.heap) - 1:
            return left_child
        if self.heap[left_child] < self.heap[right_child]:
            return left_child
        else:
            return right_child


stones = [0,-1]

ob = Solution()
ans = ob.lastStoneWeight(stones)
ans
