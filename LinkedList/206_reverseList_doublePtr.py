# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_list(content):

    head = ListNode(content[0], None)
    ptr = head

    for i in content[1:]:

        ptr.next = ListNode(val=i, next=None)
        ptr = ptr.next

    return head

def print_list(head: ListNode) -> [int]:

    array = []
    cur = head

    while cur:
        array.append(cur.val)
        cur = cur.next
    
    return array


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        slow = None
        fast = head

        while fast:

            temp = fast.next
            fast.next = slow
            slow = fast
            fast = temp
        
        return slow
            
            

head = create_list([1, 2, 3, 4, 5])

ob = Solution()
ans = print_list(ob.reverseList(head))

ans

'''
方法1.  双指针 pre, cur: cur一直往前走，pre在后面走

        cur和pre交换位置，就是.next操作
        此时要注意保护cur前进位置的元素保存

        为什么最后不需要对原head(现在的尾结点)进行.next==none操作
        因为本质上，都是none
        null -> 1 -> 2 -> 3 -> 4 -> 5 -> null


'''
