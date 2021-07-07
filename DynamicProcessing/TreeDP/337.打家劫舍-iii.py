#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    @lru_cache(None)
    def rob(self, root: TreeNode) -> int:

        # root + root.left.left + root.left.right + root.right.left + root.right.right
        # root.left + root.right

        if not root:
            return 0
        
        grand_money = root.val
        
        if root.left:
            grand_money = grand_money + self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            grand_money = grand_money + self.rob(root.right.left) + self.rob(root.right.right)
        
        father_money = self.rob(root.left) + self.rob(root.right)

        self.ans = max(grand_money, father_money)

        return self.ans
            
# @lc code=end

