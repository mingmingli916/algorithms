"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).



Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100


Follow up: Could you solve it both recursively and iteratively?
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.answer = True

    def isSymmetric(self, root: TreeNode) -> bool:
        # base case
        if root is None:
            return True

        self.answer = True
        self.isSymmetricHelper(root, root)
        return self.answer

    def isSymmetricHelper(self, l: TreeNode, r: TreeNode):
        if l.left and r.right:
            self.answer = self.answer and (l.left.val == r.right.val)
        elif l.left:
            self.answer = False
        elif r.right:
            self.answer = False

        if self.answer is False:
            return

        if l.left and r.right:
            self.isSymmetricHelper(l.left, r.right)
        if l.right and r.left:
            self.isSymmetricHelper(l.right, r.left)

