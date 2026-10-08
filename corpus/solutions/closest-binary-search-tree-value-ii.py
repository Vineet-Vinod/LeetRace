class Solution:
    def closestKValues(
        self, root: Optional[TreeNode], target: float, k: int
    ) -> List[int]:
        values = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node is not None:
                values.append(node.val)
                stack.extend((node.left, node.right))
        return sorted(
            sorted(values, key=lambda value: (abs(value - target), value))[:k]
        )
