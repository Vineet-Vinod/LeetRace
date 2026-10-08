class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def inspect(node: Optional[TreeNode]) -> Tuple[bool, int, int, int]:
            if node is None:
                return True, 0, float("inf"), float("-inf")
            left_valid, left_size, left_min, left_max = inspect(node.left)
            right_valid, right_size, right_min, right_max = inspect(node.right)
            if left_valid and right_valid and left_max < node.val < right_min:
                size = left_size + right_size + 1
                return True, size, min(left_min, node.val), max(right_max, node.val)
            return False, max(left_size, right_size), float("-inf"), float("inf")

        return inspect(root)[1]
