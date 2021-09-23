def is_deleted(root, ans, to_delete):
    if root.left is not None:
        if is_deleted(root.left, ans, to_delete):
            root.left = None
    if root.right is not None:
        if is_deleted(root.right, ans, to_delete):
            root.right = None

    if root.val not in to_delete:
        return False
    
    to_delete.remove(root.val)
    if root.left:
        ans.append(root.left)
    if root.right:
        ans.append(root.right)
    return True


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ans = []
        if not is_deleted(root, ans, set(to_delete)):
            ans.append(root)
        return ans
