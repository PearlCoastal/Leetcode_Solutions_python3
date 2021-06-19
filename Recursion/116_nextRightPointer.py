
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
'''
def createTree(array: [int]) -> TreeNode:

    def level(index: int):

        if index >= len(array) or array(index) is None:
            return None
        
        root = Node(array[index])
        root.left = level(2*index + 1)
        root.right = level(2*index + 2)
        
        return root
    
    return level(0)
'''

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root: return None
        connect2node(root.left, root.right)
        return root
        

        def connect2node(node1: Node, node2: Node) -> Node:

            if not node1 or not node2: return

            node1.next = node2

            self.connect2node(node1.left, node1.right)
            self.connect2node(node2.left, node2.right)
            self.connect2node(node1.right, node2.left)


