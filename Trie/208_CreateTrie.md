LC.208 Implement Trie Prefix Tree
====
https://leetcode-cn.com/problems/implement-trie-prefix-tree/

	Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。
	请你实现 Trie 类：
	Trie() 初始化前缀树对象。
	void insert(String word) 向前缀树中插入字符串 word 。
	boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
	boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
	示例：
	输入
	["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
	[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
	输出
	[null, null, true, false, true, null, true]
	解释
	Trie trie = new Trie();
	trie.insert("apple");
	trie.search("apple");   // 返回 True
	trie.search("app");     // 返回 False
	trie.startsWith("app"); // 返回 True
	trie.insert("app");
	trie.search("app");     // 返回 True

## 思路


## 代码
```python
class TrieNode:
    def __init__(self):
        self.isWord = False
        self.prefixCount = 0
        self.children = {}
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for character in word:
            if character not in node.children:
                node.children[character] = TrieNode()
            node = node.children[character]
            node.prefixCount += 1
        node.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.isWord


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for character in prefix:
            if character not in node.children:
                return False
            node = node.children[character]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```
## 复杂度分析

1. **插入 和 查询**
	- 时间复杂度： O(len(key), key 是待插入（查找）的字符串。

2. **建树**
	- 时间复杂度： O(M^N), M 是字符集中字符的个数， N 是字符串长度。
