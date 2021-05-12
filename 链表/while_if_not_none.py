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

    def while_difference(self, head: ListNode) -> ListNode:

        nothead, isnotnone = head, head
        while isnotnone is not None:

            isnotnone = isnotnone.next
        
        while not nothead:
            nothead = nothead.next
        
        isnotnone

        nothead

head = createList([1,2,3,4])

ob = Solution()
ans = printList(ob.while_difference(head))

ans