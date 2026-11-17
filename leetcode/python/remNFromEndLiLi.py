# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        if n == 1:
            if head.next == None:
                return None
            temp = head
            while temp.next.next != None:
                temp = temp.next
            temp.next = None
            
            return head
        
        temp = head
        length = 0
        while temp != None:
            temp = temp.next
            length += 1
        
        if length == n:
            head = head.next
        else:        
            temp = head
            for i in range(length-n-1):
                temp = temp.next
            
            temp2 = temp.next.next
            temp.next = temp2
            
        return head

    
head = Solution().removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3))), 3)

temp = head
while temp != None:
    print(temp.val)
    temp = temp.next