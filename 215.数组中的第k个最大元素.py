#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        '''
        最小堆， 堆顶为第 k 个最大的元素
        如果有新的值 大于 堆顶， 入堆
        '''
        self.k = k
        self.heap = [0]
        for i in range(len(nums)):
            if len(self.heap) < self.k + 1:
                self.heappush(nums[i])

            else:
                if self.heap[1] < nums[i]:
                    self.heappop()
                    self.heappush(nums[i])
        return self.heap[1]

    def heappush(self, num):
        self.heap.append(num)
        self.shift_up(len(self.heap) - 1)
    
    def shift_up(self, i):
        while i // 2 > 0:
            if self.heap[i] < self.heap[i//2]:
                self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i // 2


    def heappop(self):
        if self.heap == 1:
            return None
        self.heap[1] = self.heap[len(self.heap) - 1]
        self.heap.pop()
        self.shift_down(1)
    
    def shift_down(self, i):
        while i * 2 <= len(self.heap) - 1:
            min_child = self.minChild(i)
            if self.heap[i] > min_child:
                self.heap[i], self.heap[min_child] = self.heap[min_child], self.heap[i]
            i = min_child
    
    def minChild(self, i):
        left_child = i * 2
        right_child = i * 2 + 1
        if right_child > len(self.heap) - 1:
            return left_child
        if nums[left_child] < nums[right_child]:
            return left_child
        else:
            return right_child

# @lc code=end

nums = [3,2,1,5,6,4]
k = 2

nums =[3,2,3,1,2,4,5,5,6]
k = 4

nums = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
k = 20

ob = Solution()
ans = ob.findKthLargest(nums, k)
ans