

class Solution:
    def numTrees(self, n: int) -> int:
        
        self.memo = {}
        return self.countTrees(1, n)
    
    def countTrees(self, lo: int, hi: int):

        count, index = 0, lo
        
        if lo >= hi: return 1

        if self.memo[lo][hi] != -1:

        while index != hi:

            left = self.countTrees(lo, index)
            
            right = self.countTrees(index + 1, hi)

            count += left * right
            index += 1
        
        self.memo[lohi] = count
        return count

n = 3

ob = Solution()
ans = ob.numTrees(n)

ans

