# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head    

        count = 0
        temp = head
        while temp != None:
            temp = temp.next
            count += 1

        k = k % count

        if k == 0:
            return head

        pivot_index = count - k

        index = 0
        new_head = head
        cut_node = None
        while index != pivot_index:
            cut_node = new_head
            new_head = new_head.next
            index += 1
        
        if index > 0:
            cut_node.next = None
            temp = new_head
            while temp.next != None:
                temp = temp.next
            temp.next = head

        return new_head 

# https://leetcode.com/problems/rotate-list/description/

