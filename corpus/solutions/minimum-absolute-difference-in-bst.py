class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values: list[int] = []
        stack = []
        node = root
        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            values.append(node.val)
            node = node.right
        return min(values[index] - values[index - 1] for index in range(1, len(values)))
