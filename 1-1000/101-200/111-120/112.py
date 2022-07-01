from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def find(node, target):
            if node is None:
                return False

            target -= node.val
            if target == 0 and node.left is None and node.right is None:
                return True

            return find(node.left, target) or find(node.right, target)

        return find(root, targetSum)
