# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dictionary = {}
        temp = head

        while temp != None:
            if temp.val not in dictionary.keys():
                dictionary[temp.val] = [temp]
            else:
                if temp in dictionary[temp.val]:
                    return True
                dictionary[temp.val].append(temp)
            temp = temp.next
            
        return False           

# https://leetcode.com/problems/linked-list-cycle/

