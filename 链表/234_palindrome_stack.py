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

        cur = head
        stack = []
        while cur:
            stack.append(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            if stack.pop() != cur.val: return False
            
            cur = cur.next
        return True


# head = createList([1,2,2,1])
head = createList([1,2])

ob = Solution()
ans = ob.isPalindrome(head)

ans
        