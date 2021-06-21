# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_list(content):

    head = ListNode(val=content[0], next=None)
    ptr = head

    for i in content[1:]:

        ptr.next = ListNode(val=i, next=None)
        ptr = ptr.next
    
    return head

def printList(head: ListNode) -> [int]:

    array = []
    cur = head

    while cur:
        array.append(cur.val)
        cur = cur.next
    
    return array




class Solution:

    connector = ListNode(0, None)

    def reverseNthNode(self, head: ListNode, n: int) -> ListNode:

        global connector
        if(n == 1):
            
            connector = head.next
            return head

        reverse_head = self.reverseNthNode(head.next, n-1)

        head.next.next = head
        head.next = connector

        return reverse_head
        
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        if (m == 1): return self.reverseNthNode(head, n)

        head.next = self.reverseBetween(head.next, m-1, n-1)

        return head





head = create_list([1, 2, 3, 4, 5, 6])
head = create_list([])

ob = Solution()

ans = printList(ob.reverseBetween(head, 3, 6))

ans
