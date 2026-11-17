class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        l1 = []
        l2 = []

        current_node = list1
        while current_node:
            l1.append(current_node.val)
            current_node = current_node.next

        current_node = list2
        while current_node:
            l2.append(current_node.val)
            current_node = current_node.next

        li = l1 + l2

        li.sort()

        output = ListNode(li[0])
        current_node = output
        for i in li[1:]:
            node = ListNode(i)
            current_node.next = node
            current_node = current_node.next

        return output
    
    
li1 = ListNode(1, ListNode(3, ListNode(5, ListNode(7))))
li2 = ListNode(2, ListNode(4, ListNode(6, ListNode(8))))

current_node = Solution().mergeTwoLists(li1, li2)
while current_node:
    print(current_node.val)
    current_node = current_node.next
    
# https://leetcode.com/problems/merge-two-sorted-lists/
