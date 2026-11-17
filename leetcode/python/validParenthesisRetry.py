class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        
    def insertAtStart(self, node):
        node.next = self.head
        self.head = node

    def removeFromStart(self):
        if self.head == None:
            return -1
        else:
            self.head = self.head.next
    

class Stack:
    def __init__(self):
        self.length = 0
        self.data = LinkedList()
        
    def push(self, val):
        self.data.insertAtStart(Node(val))
        self.length += 1
        
    def remove(self):
        self.data.removeFromStart()
        self.length -= 1
        
    def peek(self):
        return self.data.head.val


class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        for i in s:
            if i in ["(", "{", "["]:
                stack.push(i)
            else:
                if stack.length == 0:
                    return False
                elif i == ")":
                    if stack.peek() != "(":
                        return False
                    else:
                        stack.remove()
                elif i == "]":
                    if stack.peek() != "[":
                        return False
                    else:
                        stack.remove()
                else:
                    if stack.peek() != "{":
                        return False
                    else:
                        stack.remove()
    
        if stack.length != 0:
            return False
        else:
            return True

print(Solution().isValid(r"("))