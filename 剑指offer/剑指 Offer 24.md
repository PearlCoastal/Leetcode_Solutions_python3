剑指 Offer 24. 反转链表
====
https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/

> [方法一： 迭代](https://github.com/PearlCoastal/Leetcode_GitOn/new/master/%E5%89%91%E6%8C%87offer#%E6%96%B9%E6%B3%95%E4%B8%80-%E8%BF%AD%E4%BB%A3)<br>
> [方法二： 递归](https://github.com/PearlCoastal/Leetcode_Solutions_python3/blob/master/%E5%89%91%E6%8C%87offer/%E5%89%91%E6%8C%87%20Offer%2024.md#%E6%96%B9%E6%B3%95%E4%BA%8C-%E9%80%92%E5%BD%92)<br>

## 题目描述

<img width="652" alt="截屏0003-08-09 21 14 56" src="https://user-images.githubusercontent.com/10908630/128704569-5b4acfae-3726-402b-8188-9a702ef2d30c.png">


方法一： 迭代
====

## 思路

双指针 slow fast

fast 走在前面， 将 fast 的 next 指向 slow。

然后继续往前走， 用 temp 保存 fast 的下一步节点值。

## 代码
```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow, fast = None, head
        
        while fast:
            temp = fast.next
            fast.next = slow
            slow = fast 
            fast = temp
        return slow
```

## 复杂度分析
- 时间复杂度： O(n)
- 空间复杂度： O(1)



方法二： 递归
====

## 思路

递归出口： 尾节点之后终止。

从 head 的下一个节点开始反转链表， 以防万一出错嘛。

然后拼接链表。


## 代码
```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
```

## 复杂度分析
- 时间复杂度： O(n)
- 空间复杂度： O(n) 递归栈的深度
