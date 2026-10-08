class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        best = 0

        def visit(node, minimum, maximum):
            nonlocal best
            if node is None:
                return
            best = max(best, abs(node.val - minimum), abs(node.val - maximum))
            minimum = min(minimum, node.val)
            maximum = max(maximum, node.val)
            visit(node.left, minimum, maximum)
            visit(node.right, minimum, maximum)

        visit(root, root.val, root.val)
        return best
