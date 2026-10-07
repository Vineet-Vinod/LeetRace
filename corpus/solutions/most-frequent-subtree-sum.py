class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> list[int]:
        frequencies: Counter[int] = Counter()
        subtree_sums: dict[int, int] = {}
        stack = [(root, False)] if root is not None else []
        while stack:
            node, visited = stack.pop()
            if not visited:
                stack.append((node, True))
                if node.right is not None:
                    stack.append((node.right, False))
                if node.left is not None:
                    stack.append((node.left, False))
            else:
                total = (
                    node.val
                    + subtree_sums.get(id(node.left), 0)
                    + subtree_sums.get(id(node.right), 0)
                )
                subtree_sums[id(node)] = total
                frequencies[total] += 1
        if not frequencies:
            return []
        highest = max(frequencies.values())
        return sorted(total for total, count in frequencies.items() if count == highest)
