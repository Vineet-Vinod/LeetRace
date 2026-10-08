class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        values = []
        node = head
        while node is not None:
            values.append(node.val)
            node = node.next

        def build(left: int, right: int) -> Optional[TreeNode]:
            if left >= right:
                return None
            middle = (left + right) // 2
            root = TreeNode(values[middle])
            root.left = build(left, middle)
            root.right = build(middle + 1, right)
            return root

        return build(0, len(values))
