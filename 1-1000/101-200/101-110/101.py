from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSym(left_node, right_node):
            if left_node is None or right_node is None:
                if left_node is not None or right_node is not None:
                    return False
                return True
            if left_node.val != right_node.val:
                return False
            if not isSym(left_node.left, right_node.right):
                return False
            if not isSym(left_node.right, right_node.left):
                return False
            return True
        return isSym(root.left, root.right)
