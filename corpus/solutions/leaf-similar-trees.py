class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaves(root):
            if root is None:
                return []
            if root.left is None and root.right is None:
                return [root.val]
            return leaves(root.left) + leaves(root.right)

        return leaves(root1) == leaves(root2)
