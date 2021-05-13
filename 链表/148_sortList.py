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
    def sortList(self, head: ListNode) -> ListNode:

        if not head or not head.next: return head

        mid = self.middleNode(head)

        left = self.sortList(head)
        right = self.sortList(mid)

        res = self.mergeSortedList(left, right)

        return res
    
    def middleNode(self, head: ListNode) -> ListNode:

        if not head or not head.next: return head

        slow, fast = head, head.next

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None

        return mid

    def mergeSortedList(self, left: ListNode, right: ListNode) -> ListNode:

        while left or right:
            if not left: return right
            if not right: return left

            if left.val <= right.val:
                left.next = self.mergeSortedList(left.next, right)
                return left
            
            else:
                right.next = self.mergeSortedList(left, right.next)
                return right

# head = createList([4,2,1,3])
head = createList([-1,5,3,4,0])


ob = Solution()
ans = printList(ob.sortList(head))

ans