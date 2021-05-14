

class Solution():

    def cost(self, n: int, x: int, y: int, z: int) -> int:

        result = 0

        if (n - x - y - z) >= 0: result += 1

        if (n - x - y) >= 0: result += 1

        if (n - x - z) >= 0: result += 1

        if (n - y - z) >= 0: result += 1

        return result

ob = Solution()

ans = ob.cost(10,2,5,7)

ans