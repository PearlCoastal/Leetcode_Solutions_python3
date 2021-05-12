# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def  createList(array: [int]) -> ListNode:

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

        if head == None: return head
        if head.next == None: return head

        if head.val == head.next.val:

            while (head.next and head.val == head.next.val):
                head = head.next
            
            head = self.deleteDuplicates(head.next)
        
        else:
            head.next = self.deleteDuplicates(head.next)
        
        return head


head = createList([1, 1, 1, 2, 3])

ob =  Solution()
ans = printList(ob.deleteDuplicates(head))

ans