LC. 19 Remove Nth Node from End of List
====

> [快慢指针](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/LinkedList/19_RemoveNthNode.md#%E5%BF%AB%E6%85%A2%E6%8C%87%E9%92%88)<br>
> [栈](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/LinkedList/19_RemoveNthNode.md#%E6%A0%88)<br>

https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/

    给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

    进阶：你能尝试使用一趟扫描实现吗？
    示例 1：
    ![image](https://user-images.githubusercontent.com/10908630/125785276-e06f8c20-91be-484d-a8d6-d80e1e9d4115.png)
    输入：head = [1,2,3,4,5], n = 2
    输出：[1,2,3,5]
    示例 2：
    输入：head = [1], n = 1
    输出：[]
    示例 3：
    输入：head = [1,2], n = 1
    输出：[1]

快慢指针
====
## 思路

需要一个 `dummy head`， 避免了对头节点单独进行判断。 比如如果只有一个节点， n = 1 的话：

```python
if not head or not head.next:
    return None
```

使用快慢指针： left， right。 

初始化从 `dummy` 开始走， 使用 count = n 来保证 left 和 right 相隔 `n` 个节点。

然后 left 和 right 同步一起走。

当 right 走到 `链表尾部` 的时候， left 正好走到 倒数第 N 个节点的 `前一个节点` 。

`left.next = left.next.next` 就将该节点删除啦。

```python
# Definition for singly-linked list.
# Costruct a LinkedList
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_list(content):

    head = ListNode(content[0])
    point = head

    for i in content[1:]:
        point.next = ListNode(i)
        point = point.next

    return head

def print_list(self,head:ListNode):
        point = head

        while(point != None): 
            print("[",point.val,"]")
            point = point.next
        return head
    
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(val = 0, next = head)
        left, right = dummy, dummy
        count = n
        while count > 0:
            right = right.next
            count -= 1
            
        while right.next:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next

list1 = create_list([1])
n = 1
ob = Solution()
ans = ob.removeNthFromEnd(list1,n)
ob.print_list(ans)
```

## 复杂度分析

- 时间复杂度： O(L) L 为链表节点个数。
- 空间复杂度： O(1)


栈
====
## 思路

因为栈的性质是 先进后出 的， 所以将全部节点以此入栈， 再 出栈 n 此， 此时栈顶元素就为 待删除节点的前一个元素。

妙啊ε-(´∀｀; )

## 代码
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        dummy = ListNode(val = 0, next = head)
        ptr = dummy
        stack = []
        while ptr:
            stack.append(ptr)
            ptr = ptr.next

        for i in range(n):
            stack.pop()
        
        pre = stack[-1]
        pre.next = pre.next.next
        return dummy.next
```

## 复杂度分析

- 时间复杂度： O(L)
- 空间复杂度： O(1)
