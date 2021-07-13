#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, [lists[i].val, i])
        
        dummy = ListNode(0)
        prob = dummy

        while heap:
            val, nodeIndex = heapq.heappop(heap)
            node = lists[nodeIndex]

            prob.next = node
            prob = prob.next

            node = node.next
            lists[nodeIndex] = node

            if node:
                heapq.heappush(heap, [node.val, nodeIndex])
            
        return dummy.next
# @lc code=end

lists = [[1,4,5],[1,3,4],[2,6]]
