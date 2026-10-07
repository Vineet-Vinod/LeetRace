class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
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
        dummy = TreeNode(0)
        tail = dummy
        for value in values:
            tail.right = TreeNode(value)
            tail = tail.right
        return dummy.right
