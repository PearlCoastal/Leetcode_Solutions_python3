#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> [[str]]:
        ans = []
        board = [["." for i in range(n)] for j in range(n)]
        board

        def backtrack(board, row):
            if row == n:
                ans.append(["".join(line) for line in board])
                ans
            
            for col in range(0, n):
                if valid(board, row, col):
                    # do
                    board[row][col] = "Q"
                    backtrack(board, row + 1)
                    # undo
                    board[row][col] = "."

        def valid(board, row, col):
            for i in range(0, row):
                if board[i][col] == "Q":
                    return False
            
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1
            
            return True
        
        backtrack(board, 0)
        return len(ans)
        

# @lc code=end

n = 4

ob = Solution()
ans = ob.solveNQueens(n)

ans
