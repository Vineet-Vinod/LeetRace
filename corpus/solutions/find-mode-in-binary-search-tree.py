class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        values: list[int] = []
        stack: list[TreeNode] = []
        node = root
        while node is not None or stack:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            values.append(node.val)
            node = node.right
        counts = Counter(values)
        if not counts:
            return []
        highest = max(counts.values())
        return sorted(value for value, count in counts.items() if count == highest)
