"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:


Input: root = [1,2]
Output: [2,1]
Example 5:


Input: root = [1,null,2]
Output: [2,1]


Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # base case
        if root is None:
            return []

        # recursive call
        lst = []
        if root.left:
            lst.extend(self.postorderTraversal(root.left))
        if root.right:
            lst.extend(self.postorderTraversal(root.right))
        lst.append(root.val)

        return lst

    def postorderTraveralIterative(self, root: TreeNode) -> List[int]:
        # Base case
        if root is None:
            return []

        lst = []
        stack1, stack2 = [], []
        stack1.append(root)
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        while stack2:
            node = stack2.pop()
            lst.append(node.val)
        return lst

