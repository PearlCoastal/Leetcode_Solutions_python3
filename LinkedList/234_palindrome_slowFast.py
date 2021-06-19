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


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        if not head or not head.next: return True

        mid = self.middleNode(head)
        right = self.reverseList(mid)
        left = head
        while left and right:
            if left.val != right.val: return False

            left = left.next
            right = right.next
        
        return True

    
    def middleNode(self, head: ListNode) -> ListNode:

        if not head or not head.next: return head
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None

        return mid
    
    def reverseList(self, head: ListNode) -> ListNode:

        if not head or not head.next: return head

        newList = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return newList
        
        
# head = createList([1,2,2,1])
# head = createList([1,2,3,2,1])
# head = createList([1,2,3,4,2,1])
head = createList([1,2])


ob = Solution()
ans = ob.isPalindrome(head)

ans
        