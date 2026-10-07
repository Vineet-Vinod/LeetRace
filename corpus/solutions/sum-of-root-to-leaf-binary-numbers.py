class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        total = 0
        stack = [(root, 0)]
        while stack:
            node, prefix = stack.pop()
            value = (prefix << 1) | node.val
            if node.left is None and node.right is None:
                total += value
            else:
                if node.right is not None:
                    stack.append((node.right, value))
                if node.left is not None:
                    stack.append((node.left, value))
        return total
