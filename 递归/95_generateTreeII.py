# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> [TreeNode]:

        if not n: return []

        return self.build(1, n)
        

    def build(self, lo, hi):
        
        res = []

        if lo > hi:
            res.append(None)
            return res

        for i in range(lo, hi + 1):

            left = self.build(lo, i - 1)
            right = self.build(i + 1, hi)
            

            for l in left:
                for r in right:

                    currTree = TreeNode(i)
                    currTree.left = l
                    currTree.right = r
                    res.append(currTree)
        
        return res
        
        

n = 5
ob = Solution()
ans = ob.generateTrees(n)

ans

                    