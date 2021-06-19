# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_list(content):

    head = ListNode(content[0])
    point = head

    for i in content[1:]:
        point.next = ListNode(i)
        point = point.next

    return head




class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        len = self.length_list(head)
        point2dele = len-n+1
        point2dele

        point = head
        i=1

        if(point2dele == 1):
            # if(head.next == None):
            #     return None
            # else:
            head = head.next
                # test=head.val
                # test

        else:
            while(i < point2dele-1):
                i+=1
                point = point.next
            
            # i
            point.next = point.next.next
            # temp=point.next.val 
            # temp

        
        return head

    def print_list(self,head:ListNode):
        point = head

        while(point != None): 
            print("[",point.val,"]")
            point = point.next
        return head
    
    def length_list(self,head:ListNode)->int:

        point = head
        count = 0

        while(point != None):

            count += 1
            count
            point = point.next

        return count



list1 = create_list([1])
n = 1
ob = Solution()
ans = ob.removeNthFromEnd(list1,n)
ob.print_list(ans)
