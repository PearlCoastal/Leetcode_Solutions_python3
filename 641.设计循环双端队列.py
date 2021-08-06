#
# @lc app=leetcode.cn id=641 lang=python3
#
# [641] 设计循环双端队列
#

# @lc code=start
class ListNode:
    def __init__(self, value = None, nextNode = None):
        self.value = value
        self.next = nextNode
        self.prev = None

class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.capacity = k
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.count == self.capacity:
            return False
        if self.count == 0:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            newNode = ListNode(value)
            newNode.prev = self.tail
            newNode.next = self.head
            self.tail.next = newNode
            self.head.prev = newNode
        self.count += 1
        return True



    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.count == self.capacity:
            return False
        if self.count == 0:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            newNode = ListNode(value)
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.count += 1
        return True


    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.count == 0:
            return False
        if self.count == 1:
            self.head = None
            self.tail = None
            self.count -= 1
            return True
        new_head = self.head.next
        new_head.prev = self.tail
        self.tail.next = new_head
        self.head = new_head
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.count == 0:
            return False
        if self.count == 1:
            self.head = None
            self.tail = None
            self.count -= 1
            return True
        new_tail = self.tail.prev
        self.head.prev = new_tail
        new_tail.next = self.head
        self.tail = new_tail
        self.count -= 1
        return True


    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.head == None:
            return -1
        return self.head.value


    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.tail == None:
            return -1
        return self.tail.value

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.count == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:

# @lc code=end

obj = MyCircularDeque(3)
param_1 = obj.insertFront(1)
param_2 = obj.insertLast(2)
param_3 = obj.deleteFront()
param_4 = obj.deleteLast()
param_5 = obj.getFront()
param_6 = obj.getRear()
param_7 = obj.isEmpty()
param_8 = obj.isFull()