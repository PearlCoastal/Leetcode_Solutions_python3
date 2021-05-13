# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createList(array: [int]) -> ListNode:

    head = ListNode(array[0])
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
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # recommend middleNode
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondHead = slow.next
        slow.next = None
        
        secondList = self.reverseList(secondHead)
        
        self.merge(head, secondList)

        return head


    def reverseList(self, head: ListNode) -> ListNode:

        if(head.next == None or head == None): return head

        reverse_head = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return reverse_head

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:

        while l1 and l2:
            left = l1.next
            right = l2.next

            l1.next = l2
            l1 = left

            l2.next = l1
            l2 = right
    
        return l1


head = createList([1,2,3,4,5])

ob = Solution()
ans = printList(ob.reorderList(head))

ans