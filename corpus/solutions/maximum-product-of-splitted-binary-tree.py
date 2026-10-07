class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod = 10**9 + 7
        if root is None:
            return 0
        sums: dict[int, int] = {}
        stack: list[tuple[TreeNode, bool]] = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if visited:
                total = (
                    node.val + sums.get(id(node.left), 0) + sums.get(id(node.right), 0)
                )
                sums[id(node)] = total
            else:
                stack.append((node, True))
                if node.left is not None:
                    stack.append((node.left, False))
                if node.right is not None:
                    stack.append((node.right, False))
        total = sums[id(root)]
        best = 0
        for subtotal in sums.values():
            if subtotal != total:
                best = max(best, subtotal * (total - subtotal))
        return best % mod
