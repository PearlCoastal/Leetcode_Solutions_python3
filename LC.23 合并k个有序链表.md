LC.23 Merge K Sorted Lists
====
https://leetcode-cn.com/problems/merge-k-sorted-lists/

    给你一个链表数组，每个链表都已经按升序排列。
    请你将所有链表合并到一个升序链表中，返回合并后的链表。
    示例 1：
    输入：lists = [[1,4,5],[1,3,4],[2,6]]
    输出：[1,1,2,3,4,4,5,6]
    解释：链表数组如下：
    [
    1->4->5,
    1->3->4,
    2->6
    ]
    将它们合并到一个有序链表中得到。
    1->1->2->3->4->4->5->6
    示例 2：
    输入：lists = []
    输出：[]
    示例 3：
    输入：lists = [[]]
    输出：[]

## 思路

分治：将 k 个链表分成 `两个 两个 一对` 进行处理，调用 `LC.21 mergeTwoList()` 。

用 `堆` 实现的，我再来学习一下。

## 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        n = len(lists)

        if n == 0: return None
        if n == 1: return lists[0]
        if n == 2: return self.mergeTwoLists(lists[0], lists[1])

        mid = n // 2
        return self.mergeTwoLists(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:n]))    

    def mergeTwoLists(self, list1: List[ListNode], list2: List[ListNode]) -> ListNode:

        l1, l2 = list1, list2

        while l1 or l2:
            if not l1: return l2
            if not l2: return l1

            if l1.val <= l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2
```

## 复杂度分析：

递归的复杂度怎么算的来着？？

    - 时间复杂度：O(KN^2)
    - 空间复杂度：O(N) 递归调用栈深度
