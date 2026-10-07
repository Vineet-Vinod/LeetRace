class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_counts = Counter({0: 1})

        def count_from(node: Optional[TreeNode], prefix: int) -> int:
            if node is None:
                return 0
            current = prefix + node.val
            total = prefix_counts[current - targetSum]
            prefix_counts[current] += 1
            total += count_from(node.left, current)
            total += count_from(node.right, current)
            prefix_counts[current] -= 1
            return total

        return count_from(root, 0)
