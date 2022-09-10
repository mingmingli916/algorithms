"""
Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.



Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # base case
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # Init the head.
        if list1.val < list2.val:
            head = list1
            cur1 = list1.next
            cur2 = list2
        else:
            head = list2
            cur1 = list1
            cur2 = list2.next

        # merge
        cur = head
        while cur1 is not None and cur2 is not None:
            if cur1.val > cur2.val:
                cur.next = cur2
                cur = cur2
                cur2 = cur2.next
            else:
                cur.next = cur1
                cur = cur1
                cur1 = cur.next

        if cur1 is None:
            cur.next = cur2
        if cur2 is None:
            cur.next = cur1

        return head
