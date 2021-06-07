#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        slow, fast = head, head

        #检测链表是否有环
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        #无环， 返回none   
        if not fast or not fast.next:
            return None
        #双指针，第二轮相遇
        fast = head
        #fast 和 slow 一次走一步， 走到环入口节点
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return fast
        
# @lc code=end

