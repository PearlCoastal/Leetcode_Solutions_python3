class Solution:
    def findNumberIn2DArray(self, matrix: [[int]], target: int) -> bool:

        if not matrix:
            return 
        
        n, m = len(matrix), len(matrix[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i > n or j > m:
                return 
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                dfs(i - 1, j)
                dfs(i, j - 1)
                dfs(i - 1, j - 1)
            else:
                dfs(i + 1, j)
                dfs(i, j + 1)
                dfs(i + 1, j + 1)
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] > target:
                    i
    
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 5
ob = Solution()
ans = ob.findNumberIn2DArray(matrix, target)
ans