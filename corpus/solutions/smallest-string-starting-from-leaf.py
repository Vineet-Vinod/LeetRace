class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        best = None

        def visit(node: Optional[TreeNode], path: str) -> None:
            nonlocal best
            if node is None:
                return
            current = chr(ord("a") + node.val) + path
            if node.left is None and node.right is None:
                if best is None or current < best:
                    best = current
                return
            visit(node.left, current)
            visit(node.right, current)

        visit(root, "")
        return best or ""
