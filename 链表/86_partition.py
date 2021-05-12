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
    def partition(self, head: ListNode, x: int) -> ListNode:

        if not head or not head.next: return head

        big_head, small_head = ListNode(0), ListNode(0)
        
        big_tail, small_tail = big_head, small_head

        while head:
            if head.val < x:
                small_tail.next = head
                small_tail = small_tail.next

            else:
                big_tail.next = head
                big_tail = big_tail.next
            
            head = head.next
        
        small_tail.next = big_head.next
        big_tail.next = None

        return small_head.next

# head = createList([1,4,3,2,5,2])
head = createList([1,4,3,2,5,2,1])

ob = Solution()
ans = printList(ob.partition(head, 3))

ans