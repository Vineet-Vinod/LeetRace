class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        while node and node.val != val:
            node = node.left if val < node.val else node.right
        return node
