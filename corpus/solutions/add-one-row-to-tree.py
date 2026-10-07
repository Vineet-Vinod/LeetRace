class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)
        if root is None:
            return None
        level = [root]
        for _ in range(depth - 2):
            level = [
                child
                for node in level
                for child in (node.left, node.right)
                if child is not None
            ]
        for node in level:
            node.left = TreeNode(val, node.left, None)
            node.right = TreeNode(val, None, node.right)
        return root
