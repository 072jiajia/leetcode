from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def findDepth(node):
            if node is None:
                return 0
            return max(findDepth(node.left), findDepth(node.right)) + 1

        return findDepth(root)
