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

        self.frontier = head

        def palindromeCheck(head: ListNode) -> bool:

            tail = head
            if tail is not None:

                if not palindromeCheck(tail.next): return False

                if self.frontier.val != tail.val: return False
                self.frontier = self.frontier.next
            return True
        
        return palindromeCheck(head)


# head = createList([1,2,2,1])
# head = createList([1,2,3,2,1])
head = createList([1,2,3,4,2,1])
# head = createList([1,2])

ob = Solution()
ans = ob.isPalindrome(head)

ans
