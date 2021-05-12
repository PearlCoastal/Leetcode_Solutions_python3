
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

class Solution:

    def oddEvenList(self, head: ListNode) -> ListNode:

        if not head:
            return head
        
        evenHead = head.next

        odd = head
        even = evenHead

        while even and even.next:

            odd.next = even.next
            odd = odd.next
            
            even.next = odd.next
            even = even.next

        odd.next = evenHead

        return head
        
        


head = create_list([1,2,3,4,5])

ob = Solution()

ans = ob.oddEvenList(head)

ans

'''
1. separate odd nodes and even nodes

2. key point: when while ends

    because even is running faster than odd, so the border of the list is even

3. figure out how list pointer linked

'''