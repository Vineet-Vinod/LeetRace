class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        values = []
        stack = []
        node = root
        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            values.append(node.val)
            node = node.right

        def build(left, right):
            if left >= right:
                return None
            middle = (left + right - 1) // 2
            node = TreeNode(values[middle])
            node.left = build(left, middle)
            node.right = build(middle + 1, right)
            return node

        return build(0, len(values))
