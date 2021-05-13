class Solution:
    def hanota(self, A: [int], B: [int], C: [int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """

        length = len(A)
        self.move(length, A, B, C)

    def move(self, length: int, A: [int], B: [int], C: [int]):

        if length == 1: 
            C.append(A[-1])
            A.pop()

        else:
            self.move(length-1, A, C, B)
            C.append(A[-1])
            A.pop()
            self.move(length-1, B, A, C)



A = [2, 1, 0]
B = []
C = []

ob = Solution()
ans = ob.hanota(A, B, C)

ans
