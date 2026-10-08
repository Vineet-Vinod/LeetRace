class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        best = 0
        stack = [(root, 1)]
        while stack:
            node, length = stack.pop()
            best = max(best, length)
            if node.left is not None:
                next_length = length + 1 if node.left.val == node.val + 1 else 1
                stack.append((node.left, next_length))
            if node.right is not None:
                next_length = length + 1 if node.right.val == node.val + 1 else 1
                stack.append((node.right, next_length))
        return best
