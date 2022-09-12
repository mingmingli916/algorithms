"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:


Input: root = [1,2]
Output: [1,2]
Example 5:


Input: root = [1,null,2]
Output: [1,2]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # base case
        if root:
            return []

        lst = list()
        lst.append(root.val)
        if root.left:
            lst.extend(self.preorderTraversal(root.left))
        if root.right:
            lst.extend(self.preorderTraversal(root.right))

        return lst

    def preorderTraveralIterative(self, root: TreeNode) -> List[int]:
        # Base case
        if root is None:
            return []

        lst = list()
        node_stack = [root]
        while node_stack:
            node = node_stack.pop()
            lst.append(node.val)
            if node.right:
                node_stack.append(node.right)
            if node.left:
                node_stack.append(node.left)
        return lst


if __name__ == '__main__':
    solution = Solution()

    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    root.right = node2
    node2.left = node3
    result = solution.preorderTraveralIterative(root)
    print(result)
