class Solution:
    def maxValue(self, grid:[[int]]) -> int:
        if not grid:
            return 0
        dp = [[0 for i in range(len(grid))] for j in range(len(grid[0]))]
        a = dp[0][len(grid[0])]
        b = dp[len(grid)][0]
        a
        b

        dp[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            dp[i][0] = grid[i][0] + dp[i - 1][0]
        for j in range(1, len(grid[0])):
            dp[0][j] = grid[0][j] + dp[0][j - 1]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]

grid = [[1,2,5],[3,2,1]]

ob = Solution()
ans = ob.maxValue(grid)
ans