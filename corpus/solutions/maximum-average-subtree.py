class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        best_sum = 0
        best_count = 1

        def visit(node):
            nonlocal best_sum, best_count
            if node is None:
                return 0, 0
            left_sum, left_count = visit(node.left)
            right_sum, right_count = visit(node.right)
            total = node.val + left_sum + right_sum
            count = 1 + left_count + right_count
            if total * best_count > best_sum * count:
                best_sum, best_count = total, count
            return total, count

        visit(root)
        return best_sum / best_count
