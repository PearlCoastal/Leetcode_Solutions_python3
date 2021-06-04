#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#
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
    while not cur:
        array.append(cur.val)
        cur = cur.next
    
    return array
# @lc code=start
# Definition for singly-linked list.
#   1.  slow, fast = head, head.next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        slow, fast = head, head.next
        
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        if fast:
            return slow.next
        else:
            return slow


#   2.  slow, fast = head, head
    
'''
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        slow, fast = head, head
        
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        return slow

'''



# @lc code=end

head = createList([1,2,3,4,5,6])

ob = Solution()
ans = printList(ob.middleNode(head))
ans