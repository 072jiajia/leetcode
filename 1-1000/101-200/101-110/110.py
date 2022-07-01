from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_getDepth(node):
            if node is None:
                return True, 0
            left = check_getDepth(node.left)
            if not left[0]:
                return False, None
            right = check_getDepth(node.right)
            if not right[0]:
                return False, None
            if left[1] - right[1] in [-1, 0, 1]:
                return True, max(left[1], right[1]) + 1
            return False, None
        return check_getDepth(root)[0]
