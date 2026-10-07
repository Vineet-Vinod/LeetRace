class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        best = root.val
        node = root
        while node is not None:
            if abs(node.val - target) < abs(best - target):
                best = node.val
            elif abs(node.val - target) == abs(best - target):
                best = min(best, node.val)
            node = node.left if target < node.val else node.right
        return best
