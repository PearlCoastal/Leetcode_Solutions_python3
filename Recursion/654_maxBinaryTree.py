# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def createTree(array: [int]) -> TreeNode:

    def level(index: int):

        if index >= len(array) or array(index) is None:
            return None
        
        root = Node(array[index])
        root.left = level(2*index + 1)
        root.right = level(2*index + 2)
        
        return root
    
    return level(0)

class Solution:
    def constructMaximumBinaryTree(self, nums: [int]) -> TreeNode:
        
        length = len(nums)

        root = self.buildBinaryTree(nums, 0, length)

        return root

    def buildBinaryTree(self, nums: [int], lo: int, hi: int):
        
        if lo >= hi: return None
        
        index = lo

        for i in range(lo, hi):
            if nums[i] > nums[index]:
                index = i
        
        root = TreeNode(val= nums[index], left= None, right= None)
        root.left = self.buildBinaryTree(nums, lo, index)
        root.right = self.buildBinaryTree(nums, index + 1, hi)

        return root



nums = [3,2,1,6,0,5]

ob = Solution()
ans = ob.constructMaximumBinaryTree(nums)

ans
