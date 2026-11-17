# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        elif head.next.next == None:
            temp = head.next
            temp.next = head
            head.next = None
            return temp
            

        temp1 = head.next
        temp2 = head.next.next
        head.next = None
        
        while temp2:
            temp1.next = head
            head = temp1
            temp1 = temp2
            temp2 = temp1.next
        temp1.next = head
        head = temp1

        return head


# https://leetcode.com/problems/reverse-linked-list/

