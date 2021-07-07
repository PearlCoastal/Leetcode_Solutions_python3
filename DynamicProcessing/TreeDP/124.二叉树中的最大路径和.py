#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        self.ans = float('-inf')

        def dfs(root: TreeNode) -> int:
            if not root: return 0

            left_sum = max(0, dfs(root.left))
            right_sum = max(0, dfs(root.right))
            
            self.ans = max(self.ans, root.val + left_sum + right_sum)

            return root.val + max(left_sum, right_sum)

        dfs(root)
        return self.ans

# @lc code=end

