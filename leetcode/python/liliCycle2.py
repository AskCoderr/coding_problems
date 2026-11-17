# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        # finding whether a cycle exists in the linked list
       
        if head == None or head.next == None:
            return None

        hasCycle = False
        slow_pointer = fast_pointer = head

        while fast_pointer.next != None and fast_pointer.next.next != None:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
            
            if slow_pointer == fast_pointer:
                hasCycle = True
                break

        if not hasCycle:
            return None

        # finding length of the cycle
        
        cycle_length = 1
        temp = slow_pointer.next
        while temp != slow_pointer:
            temp = temp.next
            cycle_length += 1

        # finding first node in cycle
        
        temp1 = head
        temp2 = temp1

        for i in range(cycle_length):
            temp2 = temp2.next

        temp3 = temp2

        if temp2 == temp1:
            return temp1

        while True:
            for i in range(cycle_length):
                temp3 = temp3.next
            
            if temp3 == temp2:
                break
            else:
                temp1 = temp2
                temp2 = temp3
            
        while True:
            temp1 = temp1.next
            temp4 = temp1

            for i in range(cycle_length):
                temp4 = temp4.next
            
            if temp1 == temp4:
                return temp1


# https://leetcode.com/problems/linked-list-cycle-ii/description/

