class Solution:
    def insertIntoMaxTree(
        self, root: Optional[TreeNode], val: int
    ) -> Optional[TreeNode]:
        node = root
        previous = None
        while node is not None and node.val > val:
            previous = node
            node = node.right
        inserted = TreeNode(val, node, None)
        if previous is None:
            return inserted
        previous.right = inserted
        return root
