class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def height(node: Optional[TreeNode]) -> int:
            nonlocal diameter
            if node is None:
                return 0
            left = height(node.left)
            right = height(node.right)
            diameter = max(diameter, left + right)
            return max(left, right) + 1

        height(root)
        return diameter
