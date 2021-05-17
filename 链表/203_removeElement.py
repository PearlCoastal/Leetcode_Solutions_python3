# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createList(array: [int]) -> ListNode:

    head = ListNode(val= array[0], next= None)
    ptr = head

    for element in array[1:]:
        ptr.next = ListNode(val= element, next= None)
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
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        if not head: return head

        dummy = ListNode(val= 0, next= head)

        cur = dummy

        while cur.next:

            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        
        return dummy.next

head = createList([7,7,7,7])
val = 7

ob = Solution()
ans = printList(ob.removeElements(head, val))

ans