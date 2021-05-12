# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def createList(content):

    head = ListNode(val=content[0], next=None)
    ptr = head

    for i in content[1:]:

        ptr.next = ListNode(val=i, next=None)
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
    def hasCycle(self, head: ListNode) -> bool:

        if not head or not head.next: return False

        slow, fast = head, head.next

        while slow != fast:

            if not fast or not fast.next: return False
            slow = slow.next
            fast = fast.next.next
        
        return True