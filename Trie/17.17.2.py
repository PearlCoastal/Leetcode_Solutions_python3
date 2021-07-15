
from collections import defaultdict
class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.pos = []


class Solution:
    def multiSearch(self, big: str, smalls: [str]) -> [[int]]:
        self.root = Node()

        def search(s):
            cur = self.root
            for idx, char in enumerate(s):
                if char not in cur.children:
                    return []
                cur = cur.children[char]
            return cur.pos
        
        def insert(start, s):
            cur = self.root
            for idx, char in enumerate(s):
                cur.children[char].pos.append(start)
                cur = cur.children[char]
        
        for i in range(len(big)):
            insert(i, big[i:])
        
        ans = []
        for word in smalls:
            ans.append(search(word))
        
        return ans

big = "mississippi"
smalls = ["is","ppi","hi","sis","i","ssippi"]

obj = Solution()
ans = obj.multiSearch(big, smalls)
ans