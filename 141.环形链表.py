#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        if not head:
            return False
        
        slow, fast = head, head.next

        if fast == None:
            return False
        
        while fast and fast.next:

            if slow == fast:
                return True

            slow = slow.next
            fast = fast.next.next
            
        return False
# @lc code=end

