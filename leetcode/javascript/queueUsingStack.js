class Stack {
    constructor() {
        this.array = [];
        this.length = 0;
    }
    peek() {
        return this.array[this.array.length-1];
    }
    push(value) {
        this.array.push(value);
        this.length++;
    }
    pop() {
        if (this.length === 0) {
            console.log("stack is empty");
        } else {
            this.length--;
            return this.array.pop();
        }
    }
}

var MyQueue = function() {
    this.stack = new Stack();
    this.reversedStack = new Stack();
};

/** 
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function(x) {
    while (this.reversedStack.length != 0) {
        y = this.reversedStack.pop();
        this.stack.push(y);
    }
    this.stack.push(x);
};

/**
 * @return {number}
 */
MyQueue.prototype.pop = function() {
    while (this.stack.length != 0) {
        y = this.stack.pop();
        this.reversedStack.push(y);
    }
    return this.reversedStack.pop();
};

/**
 * @return {number}
 */
MyQueue.prototype.peek = function() {
    while (this.stack.length != 0) {
        y = this.stack.pop();
        this.reversedStack.push(y);
    }
    return this.reversedStack.peek();
};

/**
 * @return {boolean}
 */
MyQueue.prototype.empty = function() {
    if ((this.stack.length === 0) && (this.reversedStack.length === 0)) {
        return true;
    } else {
        return false;
    }
};


/** 
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */

// https://leetcode.com/problems/implement-queue-using-stacks/