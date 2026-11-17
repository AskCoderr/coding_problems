# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head):
        counter = 1
        temp = head
        while temp.next != None:
            temp = temp.next
            counter += 1
        
        if counter % 2 != 0:
            counter = counter // 2
        else: 
            counter = int(counter / 2)
        
        temp = head
        for i in range(counter):
            temp = temp.next

        return temp
    
node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
ret = (Solution().middleNode(node))
while ret != None:
    print(ret.val)
    ret = ret.next

# https://leetcode.com/problems/middle-of-the-linked-list/