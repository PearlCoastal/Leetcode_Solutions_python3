LC.23 Reverse k group
====

## 思路

分治：将 k 个链表分成 `2个 2个 一对`，然后调用 `LC.21 mergeTwoLists()`。 

看到评论里有用 `堆` 做的，我再去学习一下怎么用堆写这道题。

之前一看到 medium 题加个 k 摇身一变 hard 就吓得要死， 现在学了分治，有胆子了。٩(˃̶͈̀௰˂̶͈́)و

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

## 复杂度分析
递归的复杂度怎么分析的来着！(◎_◎;)

- 时间复杂度：O(KN^2)
- 空间复杂度：O(N) 递归调用栈的大小

## 思路
最小堆
## 代码
```python
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, [lists[i].val, i])
        
        dummy = ListNode(0)
        prob = dummy

        while heap:
            val, nodeIndex = heapq.heappop(heap)
            node = lists[nodeIndex]

            prob.next = node
            prob = prob.next

            node = node.next
            lists[nodeIndex] = node

            if node:
                heapq.heappush(heap, [node.val, nodeIndex])
            
        return dummy.next
```