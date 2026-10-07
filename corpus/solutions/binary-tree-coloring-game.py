class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        left_count = right_count = 0

        def count(node: Optional[TreeNode]) -> int:
            nonlocal left_count, right_count
            if node is None:
                return 0
            left = count(node.left)
            right = count(node.right)
            if node.val == x:
                left_count, right_count = left, right
            return left + right + 1

        count(root)
        parent_side = n - left_count - right_count - 1
        return max(left_count, right_count, parent_side) > n // 2
