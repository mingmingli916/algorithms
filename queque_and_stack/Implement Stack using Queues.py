'''
Implement a last in first out (LIFO) stack using only two queues.
The implemented stack should support all the functions of a normal queue (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue,
which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, the queue may not be supported natively.
You may simulate a queue using a list or deque (double-ended queue),
as long as you use only a queue's standard operations.


Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False


Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.


Follow-up:
Can you implement the stack such that each operation is amortized O(1) time complexity?
In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.
You can use more than two queues.
'''
import collections


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Used for push.
        self.normal_queue = collections.deque()
        # Used for pop and top
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.normal_queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while self.normal_queue:
            x = self.normal_queue.popleft()
            # The queue1 and queue2 are used to reverse normal_queue.
            if not self.queue1:
                self.queue1.append(x)
                while self.queue2:
                    self.queue1.append(self.queue2.popleft())
            else:
                self.queue2.append(x)
                while self.queue1:
                    self.queue2.append(self.queue1.popleft())

        if self.queue1:
            return self.queue1.popleft()
        if self.queue2:
            return self.queue2.popleft()

        return None

    def top(self) -> int:
        """
        Get the top element.
        """
        while self.normal_queue:
            x = self.normal_queue.popleft()
            if not self.queue1:
                self.queue1.append(x)
                while self.queue2:
                    self.queue1.append(self.queue2.popleft())
            else:
                self.queue2.append(x)
                while self.queue1:
                    self.queue2.append(self.queue1.popleft())

        if self.queue1:
            return self.queue1[0]
        if self.queue2:
            return self.queue2[0]
        return None

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not (self.normal_queue or self.queue1 or self.queue2)


if __name__ == '__main__':
    # Your MyStack object will be instantiated and called as such:
    obj = MyStack()
    obj.push(1)
    param_2 = obj.pop()
    # param_3 = obj.top()
    param_4 = obj.empty()
    print(param_4)
