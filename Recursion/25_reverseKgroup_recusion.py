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


class Solution():
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        if not head: return head

        tail = head

        for check_length in range(k-1):

            tail = tail.next
            if not tail: return head
        
        nextNode = tail.next
        tail.next = None

        newHead = self.reverse(head)
        # head.next = nextNode
        head.next = self.reverseKGroup(nextNode, k)

        return newHead

    def reverse(self, head: ListNode):

        pre = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur 
            cur = temp
        return pre


head = createList([1, 2, 3, 4, 5])
ob = Solution()
ans = printList(ob.reverseKGroup(head, 3))

ans