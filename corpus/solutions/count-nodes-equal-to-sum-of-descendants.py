class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        matches = 0
        subtree_sums: dict[int, int] = {}
        stack: list[tuple[TreeNode, bool]] = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if not visited:
                stack.append((node, True))
                if node.right is not None:
                    stack.append((node.right, False))
                if node.left is not None:
                    stack.append((node.left, False))
                continue
            descendants = 0
            if node.left is not None:
                descendants += subtree_sums[id(node.left)]
            if node.right is not None:
                descendants += subtree_sums[id(node.right)]
            if node.val == descendants:
                matches += 1
            subtree_sums[id(node)] = node.val + descendants
        return matches
