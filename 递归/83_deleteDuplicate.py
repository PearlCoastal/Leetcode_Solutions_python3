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
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if not head or not head.next: return head

        if head.val == head.next.val:

            while head.next and head.val == head.next.val:
                head.next = head.next.next
            
        head.next = self.deleteDuplicates(head.next)

        return head

head = createList([1,1,1,2,3,3])

ob = Solution()
ans = printList(ob.deleteDuplicates(head))

ans