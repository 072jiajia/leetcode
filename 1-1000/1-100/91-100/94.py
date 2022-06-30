from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traverse_list = []

        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            traverse_list.append(node.val)
            traverse(node.right)

        traverse(root)
        return traverse_list
