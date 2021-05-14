# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_list(content):

    head = ListNode(content[0])
    ptr = head
    for i in content[1:]:
        ptr.next = ListNode(i)
        ptr = ptr.next
        
    return head

l1 = create_list([2,4,3])
l2 = create_list([5,6,4,8,9])
               
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = curr = ListNode()
        carry = val = 0

        while carry or l1 or l2:
            val = carry

            if l1: 
                l1 = l1.next
                val = l1.val + val
    
            if l2: 
                l2 = l2.next
                val = l2.val + val

            #
            # divmod:(a // b, a % b)
            
            carry, val = divmod(val, 10)
            curr.next = curr = ListNode(val)
        
        return head.next