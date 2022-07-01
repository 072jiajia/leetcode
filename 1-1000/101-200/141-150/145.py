from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversed_list = []

        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            traverse(node.right)
            traversed_list.append(node.val)

        traverse(root)
        return traversed_list
