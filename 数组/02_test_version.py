class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

[2,4,3]
[5,6,4,8,9]


def create_list(content):

    head = ListNode(content[0])
    ptr = head
    for i in content[1:]:
        ptr.next = ListNode(i)
        ptr = ptr.next
        
    return head



class Solution():

    def add2numbers(self,l1:ListNode,l2:ListNode)->ListNode:

        head = point = ListNode(0)
        carry = 0

        while(l1 or l2):
            
            new_point = ListNode(0)

            if(l1 == None):
                sum_ = l2.val + carry
                sum_
                new_point.val = sum_ % 10
                test=new_point.val
                test
                carry = sum_ // 10
                carry
                l2 = l2.next
            
            elif(l2 == None):
                sum_ = l1.val + carry
                sum_
                new_point.val = sum_ % 10
                test=new_point.val
                test
                carry = sum_ // 10
                carry
                l1 = l1.next

            else:
                sum_ = l1.val + l2.val + carry
                sum_
                new_point.val = sum_ % 10
                test=new_point.val
                test
                carry = sum_ // 10
                carry

                l1 = l1.next
                l2 = l2.next
            
            point.next = new_point
            point = point.next

        if(carry==1):
            carry
            new_point = ListNode(1)
            test = new_point.val
            test
            point.next = new_point

        return head.next

    # def print_list(self,head:ListNode):
    #     p = head

    #     while(p != None):
    #         val = p.val
    #         val
    #         p = p.next

 

l1 = create_list([2,2,5])
l2 = create_list([5,6,5,9])

# temp2 = l1.val
# temp2 = l1.next.val        
# temp2 = l1.next.next.val
# temp2
# temp = l2.val
# temp = l2.next.val        
# temp = l2.next.next.val
# temp = l2.next.next.next.val
# temp = l2.next.next.next.next.val
# temp

ob = Solution()
print(ob.add2numbers(l1,l2))
# print(ob.print_list(l1))
