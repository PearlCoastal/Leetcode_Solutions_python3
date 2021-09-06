class Solution:
    def exist(self, board: [[str]], word: str) -> bool:

        def dfs(i, j, k):
            if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1 or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            ans = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            return ans

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
    


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

ob = Solution()
ans = ob.exist(board, word)
ans