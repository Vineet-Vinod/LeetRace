class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        pattern = []
        node = head
        while node is not None:
            pattern.append(node.val)
            node = node.next

        def matches(tree, index):
            if index == len(pattern):
                return True
            if tree is None or tree.val != pattern[index]:
                return False
            return matches(tree.left, index + 1) or matches(tree.right, index + 1)

        def search(tree):
            if tree is None:
                return False
            return matches(tree, 0) or search(tree.left) or search(tree.right)

        return search(root)
