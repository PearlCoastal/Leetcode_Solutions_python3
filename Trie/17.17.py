
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['end'] = word
    
    def search(self, word: str) -> int:
        node = self.root
        res = []
        for char in word:
            if char not in node:
                break
            node = node[char]
            if 'end' in node:
                res.append(node['end'])
        return res
import collections
class Solution:
    def multiSearch(self, big: str, smalls: [str]) -> [[int]]:
        trie = Trie()
        for i in range(len(smalls)):
            trie.insert(smalls[i])
        hit = collections.defaultdict(list)

        for i in range(len(big)):
            matchs = trie.search(big[i: ])
            for word in matchs:
                hit[word].append(i)
        ans = []
        for word in smalls:
            ans.append(hit[word])
        return ans

big = "mississippi"
smalls = ["is","ppi","hi","sis","i","ssippi"]

obj = Solution()
ans = obj.multiSearch(big, smalls)
ans