from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isIdentical(p_node, q_node):
            if p_node is None or q_node is None:
                if p_node is None and q_node is None:
                    return True
                if p_node is not None or q_node is not None:
                    return False
            if p_node.val != q_node.val:
                return False
            if not isIdentical(p_node.left, q_node.left):
                return False
            if not isIdentical(p_node.right, q_node.right):
                return False
            return True
        return isIdentical(p, q)
