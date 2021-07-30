#
# @lc app=leetcode.cn id=1054 lang=python3
#
# [1054] 距离相等的条形码
#

# @lc code=start
import collections
class Solution:
    def rearrangeBarcodes(self, barcodes: [int]) -> [int]:
        self.heap = [0]
        dic = collections.defaultdict(int)
        for num in barcodes:
            dic[num] += 1
        for key in dic:
            self.heappush((-dic[key], key))
        ans = []

        while len(self.heap) > 1:
            most_freq, most_num = self.heappop()
            if len(self.heap) <= 1:
                ans.append(most_num)
                return ans
            second_freq, second_num = self.heappop()
            ans.append(most_num)
            ans.append(second_num)
            most_freq += 1
            second_freq += 1
            if most_freq  != 0:
                self.heappush((most_freq, most_num))
            if second_freq  != 0:
                self.heappush((second_freq, second_num))
        
        return ans

    def heappush(self, a):
        self.heap.append(a)
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
            if self.heap[min_child] < self.heap[i]:
                self.heap[min_child], self.heap[i] = self.heap[i], self.heap[min_child]
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

# @lc code=end

barcodes = [1,1,1,1,2,2,3,3]
 
ob = Solution()
ans = ob.rearrangeBarcodes(barcodes)
ans