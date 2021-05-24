# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

    def build(self, lo: int, hi: int):

        if lo > hi: return [None, ]

        for i in range(lo, hi + 1):

            left = self.build(lo, i-1)
            right = self.build(i+1, hi)

            for l in left:
                for r in right:

                    currTree = TreeNode(val= i, left= None, right= None)

                    