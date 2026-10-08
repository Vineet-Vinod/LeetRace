class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        total = root.val if low <= root.val <= high else 0
        if root.val > low:
            total += self.rangeSumBST(root.left, low, high)
        if root.val < high:
            total += self.rangeSumBST(root.right, low, high)
        return total
