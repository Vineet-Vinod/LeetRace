class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        matches = 0

        def totals(node: Optional[TreeNode]) -> Tuple[int, int]:
            nonlocal matches
            if node is None:
                return 0, 0
            left_sum, left_count = totals(node.left)
            right_sum, right_count = totals(node.right)
            subtree_sum = node.val + left_sum + right_sum
            subtree_count = 1 + left_count + right_count
            if node.val == subtree_sum // subtree_count:
                matches += 1
            return subtree_sum, subtree_count

        totals(root)
        return matches
