

class min_heap:
    def __init__(self, A = []):
        self.heapify(A)
    
    def heapify(self, A):
        self.h = [0] + A
        i = 1
        while i < len(self.h):
            self.shift_down(i)
            i = i + 1

    def shift_up(self, i):
        while i // 2 > 0:
            if self.h[i] < self.h[i//2]:
                self.h[i], self.h[i//2] = self.h[i//2], self.h[i]
            i = i // 2

    def shift_down(self, i):
        while (i * 2) <= len(self.h) - 1:
            min_child = self.minChild(i)
            if self.h[i] > self.h[min_child]:
                self.h[i], self.h[min_child] = self.h[min_child], self.h[i]
            i = min_child
    
    def minChild(self, i):
        left_child = i * 2
        right_child = i * 2 + 1
        if right_child > len(self.h) - 1:
            return left_child
        if self.h[left_child] < self.h[right_child]:
            return left_child
        else:
            return right_child
        

    def heappop(self):
        if len(self.h) == 1:
            return None
        pop_node = self.h[1]
        self.h[1] = self.h[(len(self.h) - 1]
        self.h.pop()
        self.shift_down(1)
        return pop_node

    def heappush(self, a):
        self.h.append(a)
        self.shift_up(len(self.h) - 1)

h = min_heap([8,3,4,5,2])

h.heappush(1)
h.heappop() # 1
h.heappop() # 2
h.heappush(1)
h.heappop() # 1
h.heappop() # 3
