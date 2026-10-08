class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        total = 0
        subtree_sums: dict[int, int] = {}
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if not visited:
                stack.append((node, True))
                if node.right is not None:
                    stack.append((node.right, False))
                if node.left is not None:
                    stack.append((node.left, False))
                continue
            left_sum = (
                subtree_sums.get(id(node.left), 0) if node.left is not None else 0
            )
            right_sum = (
                subtree_sums.get(id(node.right), 0) if node.right is not None else 0
            )
            total += abs(left_sum - right_sum)
            subtree_sums[id(node)] = node.val + left_sum + right_sum
        return total
