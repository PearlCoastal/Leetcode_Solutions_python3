# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        # if not head or not head.next: return head

        slow, fast = head, head

        while fast is not None and fast.next is not None:

            slow = slow.next
            fast = fast.next.next

            if slow == fast: break
        
        if not fast or not fast.next: return
        
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return fast


'''
1.  不需要判断链表是否只有一个节点or链表为空 

    只有在递归的时候才需要判断，因为是递归出口

2.  快慢指针找链表中间位置，都是从head出发

3.  while true  的位置，最开始写成了while not fast or not fast.next:

4.  
  
'''
