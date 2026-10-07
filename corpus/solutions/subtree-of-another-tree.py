class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(first, second):
            if first is None or second is None:
                return first is second
            return (
                first.val == second.val
                and same(first.left, second.left)
                and same(first.right, second.right)
            )

        if subRoot is None:
            return True
        if root is None:
            return False
        return (
            same(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )
