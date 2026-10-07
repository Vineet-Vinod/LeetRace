class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        downward: dict[int, int] = {}
        longest = 0
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
            left_path = 0
            right_path = 0
            if node.left is not None and node.left.val == node.val:
                left_path = downward[id(node.left)] + 1
            if node.right is not None and node.right.val == node.val:
                right_path = downward[id(node.right)] + 1
            downward[id(node)] = max(left_path, right_path)
            longest = max(longest, left_path + right_path)
        return longest
