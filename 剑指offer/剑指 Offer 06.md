剑指 Offer 06. 从尾到头打印链表
====
https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/

> [方法一： 双指针](https://github.com/PearlCoastal/Leetcode_GitOn/new/master/%E5%89%91%E6%8C%87offer#%E5%8F%8C%E6%8C%87%E9%92%88)<br>
> [方法二： 递归](https://github.com/PearlCoastal/Leetcode_GitOn/new/master/%E5%89%91%E6%8C%87offer#%E5%9B%9E%E6%BA%AF)<br>
> [方法三： 辅助栈](https://github.com/PearlCoastal/Leetcode_Solutions_python3/blob/master/%E5%89%91%E6%8C%87offer/%E5%89%91%E6%8C%87%20Offer%2006.md#%E6%96%B9%E6%B3%95%E4%B8%89-%E8%BE%85%E5%8A%A9%E6%A0%88)

## 题目描述

<img width="645" alt="截屏0003-08-09 20 26 47" src="https://user-images.githubusercontent.com/10908630/128699645-ebf75904-4026-472c-a000-ea2c6911e37d.png">

方法一： 双指针
====

## 思路
链表只能顺序遍历， 还要我倒序输出， 委实麻烦了点。

不如先挨个把节点值存到数组里， 然后数组一头一尾双指针交换元素来的方便。


( ^ ^ )/■
## 代码
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:

        ans = []
        ptr = head
        while ptr:
            ans.append(ptr.val)
            ptr = ptr.next
        left, right = 0, len(ans) - 1
        while left <= right:
            ans[left], ans[right] = ans[right], ans[left]
            left += 1
            right -= 1
        return ans
```

## 复杂度分析
- 时间复杂度： O(n) 遍历一遍链表 O(n) + O(n/2) 双指针交换节点。
- 空间复杂度： O(n) 开辟了 ans 数组先保存遍历链表的元素。

方法二： 递归
====

## 思路

来个递归函数， 先递归到链表尾部最后一个元素， 然后挨个出栈输出自己的 val。

还挺励志的。

ε-(´∀｀; )

## 代码
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:

        return self.reversePrint(head.next) + [head.val] if head else []
```
## 复杂度分析
- 时间复杂度： O(n)
- 空间复杂度： O(n) 递归栈的深度 

方法三： 辅助栈
====

## 思路
通过一个辅助栈来存储节点值。

然后利用栈的先入后出的性质实现从尾到头的打印链表。

但是在 python 中就不需要额外的数组空间去保存栈 pop() 之后的元素了， 可以直接实现倒序输出。

## 代码
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]
```
## 
## 复杂度分析
- 时间复杂度： O(n)
- 空间复杂度： O(n)
