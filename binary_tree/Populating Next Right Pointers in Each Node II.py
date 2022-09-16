"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.


Example 1:



Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation:
The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


Constraints:

The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100
"""


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # base case
        if root is None:
            return None

        level = [root]
        while level:
            length = len(level)
            deeper_level = []
            for i in range(length - 1):
                level[i].next = level[i + 1]
                if level[i].left:
                    deeper_level.append(level[i].left)
                if level[i].right:
                    deeper_level.append(level[i].right)
            if level[-1].left:
                deeper_level.append(level[-1].left)
            if level[-1].right:
                deeper_level.append(level[-1].right)

            level = deeper_level

        return root


if __name__ == '__main__':
    solution = Solution()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.left = node2
    node1.right = node3
    solution.connect(node1)
