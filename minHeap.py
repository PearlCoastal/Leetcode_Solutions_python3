

class min_heap:
    def __init__(self, A=[]):
        self.heapify(A)

    def shift_up(self, i):
        while i // 2 > 0:
            if self.h[i] < self.h[i // 2]:
                self.h[i], self.h[i//2] = self.h[i//2], self.h[i]
            i = i // 2

    def shift_down(self, i):
        while (i * 2) <= len(self.h)-1:
            mc = self.minChild(i)
            if self.h[i] > self.h[mc]:
                self.h[i], self.h[mc] = self.h[mc], self.h[i]
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > len(self.h)-1:
            return i * 2
        if self.h[i*2] < self.h[i*2+1]:
            return i * 2
        else:
            return i * 2 + 1

    def heappop(self):
        if len(self.h) == 1:
            return None
        ans = self.h[1]
        self.h[1] = self.h[len(self.h)-1]
        self.h.pop()
        self.shift_down(1)
        return ans

    def heappush(self, a):
        self.h.append(a)
        self.shift_up(len(self.h)-1)

    def heapify(self, A):
        self.h = [0] + A
        i = 1
        while (i < len(self.h)):
            self.shift_down(i)
            i = i + 1

# 使用：

h = min_heap([5, 6, 2, 3])

h.heappush(1)
h.heappop() # 1
h.heappop() # 2
h.heappush(1)
h.heappop() # 1
h.heappop() # 3
