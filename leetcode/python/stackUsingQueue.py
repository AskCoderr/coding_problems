class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
class Queue:
    def __init__(self):
        self.front = self.rear = None
        self.length = 0
        
    def enqueue(self, node):
        if self.length == 0:
            self.rear = self.front = node
            self.length += 1
        else:
            self.rear.next = node
            self.rear = node
            self.length += 1
    
    def dequeue(self):
        if self.length == 0:
            print("underflow error!")
        elif self.front == self.rear:
            temp = self.front
            self.front = self.rear = None
            self.length -= 1
            return temp
        else:
            temp = self.front
            self.front = self.front.next
            self.length -= 1
            return temp
    
    def peek(self):
        return self.front


class MyStack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
        self.state = True

    def push(self, x: int) -> None:
        if self.state:
            self.queue1.enqueue(Node(x))
        else:
            self.queue2.enqueue(Node(x))

    def pop(self) -> int:
        if self.state:
            while self.queue1.length != 1:
                temp = self.queue1.dequeue()
                self.queue2.enqueue(temp)   
            temp = self.queue1.dequeue()
            self.state = not self.state
            return temp.val
        else:
            while self.queue2.length != 1:
                temp = self.queue2.dequeue()
                self.queue1.enqueue(temp)   
            temp = self.queue2.dequeue()
            self.state = not self.state
            return temp.val

    def top(self) -> int:
        if self.state:
            if self.queue1.length == 0:
                return None
            else:
                return self.queue1.rear.val
        else:
            if self.queue2.length == 0:
                return None
            else:
                return self.queue2.rear.val
                

    def empty(self) -> bool:
        if self.state:
            if self.queue1.length == 0:
                return True
            else:
                return False
        else:
            if self.queue2.length == 0:
                return True
            else:
                return False

obj = MyStack()
obj.push(4)
obj.push(5)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print(param_2)
print(param_3)
print(param_4)