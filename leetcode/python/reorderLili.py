# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        print("original linked list -> ", end="")
        printList(head)
        length = 0
        temp = head

        while temp != None:
            temp = temp.next
            length += 1
        
        if not (length <= 2):
            if length == 3:
                temp = head.next
                head.next = temp.next
                head.next.next = temp
                temp.next = None
            else:
                if length % 2 == 0:
                    middle = (length // 2) - 1
                else:
                    middle = length // 2

                temp = head
                for i in range(middle):
                    temp = temp.next

                head2  = temp.next
                temp.next = None

                temp2 = head2.next
                temp3 = temp2.next
                head2.next = None
                while temp3 != None:
                    temp2.next = head2
                    head2 = temp2
                    temp2 = temp3
                    temp3 = temp3.next
                temp2.next = head2
                head2 = temp2
                
                temp = head
                temp2 = head2
                temp3 = temp.next
                temp4 = temp2.next

                while temp4 != None:
                    temp.next = temp2
                    temp2.next = temp3
                    temp = temp3
                    temp2 = temp4
                    temp3 = temp3.next
                    temp4 = temp4.next
                temp4 = temp.next
                temp.next = temp2

                temp2.next = temp3
        print("linked list after modification -> ", end="")       
        printList(head)

def printList(node):
    while node != None:
        print(node.val, end=" ")
        node = node.next
    print()

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
Solution().reorderList(head)

# https://leetcode.com/problems/reorder-list/

