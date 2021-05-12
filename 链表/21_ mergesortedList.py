# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_list(lists):

    head = ListNode(lists[0]) # 相当于强制转换list里面第一个元素为listnode形式
    ptr = head

    for i in lists[1:]:

        ptr.next = ListNode(i)
        ptr = ptr.next
    
    return head

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        while l1 or l2:

            if not l1: return l2
            if not l2: return l1

            if l1.val <= l2.val: 
                
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else: 
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2


        

l1 = create_list([1,2,4])
l2 = create_list([1,3,4])

ob = Solution()
ans = ob.mergeTwoLists(l1, l2)

ans

'''
1.  leetcode的链表题目，在vscode上编译的时候，要先将list手工转换成listnode --> 要自己编写几个Listnode转换函数

2.  递归：
        i.  递归出口：链表已经访问了所有元素时 --> 当链表l1 or l2 == null <-- 注意：在python中，判断语句要写成 not l1

        ii. 如何递归(递给你一只龟)
'''