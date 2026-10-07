class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths: list[str] = []

        def visit(node: Optional[TreeNode], prefix: str) -> None:
            if node is None:
                return
            current = str(node.val) if not prefix else prefix + "->" + str(node.val)
            if node.left is None and node.right is None:
                paths.append(current)
                return
            visit(node.left, current)
            visit(node.right, current)

        visit(root, "")
        return sorted(paths)
