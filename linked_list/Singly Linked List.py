"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.


Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3


Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.

"""

class Node:
    def __init__(self, val=None, rnext=None):
        self.val = val
        self.rnext = rnext  # reference next

    def __str__(self):
        return str(self.val)


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        """
        if self.length == 0 or index >= self.length:
            return -1

        node = self.head
        for i in range(index):
            node = node.rnext
        return node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        newNode = Node(val)
        newNode.rnext = self.head
        self.head = newNode
        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.length += 1
            return
        rlast = self.head
        while rlast.rnext:
            rlast = rlast.rnext
        rlast.rnext = newNode
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        if index > self.length:
            return
        elif index == self.length:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            newNode = Node(val)

            # locate
            node = self.head
            for i in range(1, index):
                node = node.rnext

            newNode.rnext = node.rnext
            node.rnext = newNode
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.length:
            return
        if index == 0:
            self.head = self.head.rnext
            self.length -= 1
            return

        node = self.head
        for i in range(1, index):
            node = node.rnext
        if node.rnext:
            node.rnext = node.rnext.rnext

        self.length -= 1

    def __str__(self):
        lst = []
        node = self.head
        lst.append(node.val)
        while node.rnext:
            node = node.rnext
            lst.append(node.val)
        return str(lst)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

if __name__ == '__main__':
    obj = MyLinkedList()

    # param_1 = obj.get(0)
    # print(param_1)
    #
    # obj.addAtHead(2)
    # obj.addAtTail(10)
    # obj.addAtHead(1)
    # obj.addAtTail(100)
    # print(obj)
    #
    # print(obj.get(0))
    # print(obj.get(1))
    # print(obj.get(3))
    # print(obj.get(4))
    #
    # print(obj)
    #
    # obj.addAtIndex(0, 0)
    # print(obj)
    #
    # obj.addAtIndex(2, 2000)
    # print(obj)
    # obj.deleteAtIndex(5)
    # print(obj)
    # obj.deleteAtIndex(1)
    # print(obj)
    # obj.deleteAtIndex(2)
    # print(obj)

    # obj.addAtTail(1)
    # print(obj.get(0))

    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtIndex(1, 2)
    obj.get(1)
    obj.deleteAtIndex(1)
    obj.get(1)
