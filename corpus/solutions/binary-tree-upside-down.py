class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        previous_root = None
        previous_right = None
        while root is not None:
            next_root = root.left
            root.left = previous_right
            previous_right = root.right
            root.right = previous_root
            previous_root = root
            root = next_root
        return previous_root
