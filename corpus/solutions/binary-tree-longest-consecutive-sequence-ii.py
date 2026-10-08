class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        best = 0

        def visit(node: Optional[TreeNode]) -> tuple[int, int]:
            nonlocal best
            if node is None:
                return 0, 0
            increasing = decreasing = 1
            if node.left is not None:
                left_inc, left_dec = visit(node.left)
                if node.left.val == node.val + 1:
                    increasing = max(increasing, left_inc + 1)
                if node.left.val == node.val - 1:
                    decreasing = max(decreasing, left_dec + 1)
            if node.right is not None:
                right_inc, right_dec = visit(node.right)
                if node.right.val == node.val + 1:
                    increasing = max(increasing, right_inc + 1)
                if node.right.val == node.val - 1:
                    decreasing = max(decreasing, right_dec + 1)
            best = max(best, increasing + decreasing - 1)
            return increasing, decreasing

        visit(root)
        return best
