剑指 Offer 52. 两个链表的第一个公共节点
====
https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/
```
输入两个链表，找出它们的第一个公共节点。

如下面的两个链表：
```
![image](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_statement.png)

```
在节点 c1 开始相交。
```
 
```
示例 1：
```
![image](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_example_1.png)

```
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
```
```
示例 2：
```
![image](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_example_2.png)

```
输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。
在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
```
```
示例 3：
```
![image](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_example_3.png)

```
输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。

```

## 思路

跟检测链表中是否有环那道题目一样。

链表因为只能逐步往后走的特点， 跟数组按下标索引不一样， 只能按照 `.next` 这样一个一个寻找。

那如何在俩链表里面找相同的元素呢？

就得一步一步数， 跟找 链表内的环 一样， 走到哪一步的时候， 如果有环的话， 再从头开始走， 走多少步， 我能走到链表环的入口。

两个链表 l1, l2 如果有相交节点的话， 
```
l1 = a + b
l2 = c + b
```
l1 走了 a + b 步之后， 从 l2 开始走
l2 走了 c + b 步之后， 从 l1 开始走

那 l1 l2 走的步数 都为 a + b + c 时， 就是相交的节点。

所以链表题嘛， 就是一个链式结构 + 数学数步数， 只是我永远都学不会

(　ﾟдﾟ)

## 代码
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        node1, node2 = headA, headB
        
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA
            
        return node1
```
