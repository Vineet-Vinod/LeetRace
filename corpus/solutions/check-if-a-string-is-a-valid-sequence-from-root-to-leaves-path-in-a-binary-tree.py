class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        def visit(node: Optional[TreeNode], index: int) -> bool:
            if node is None or index >= len(arr) or node.val != arr[index]:
                return False
            if index == len(arr) - 1:
                return node.left is None and node.right is None
            return visit(node.left, index + 1) or visit(node.right, index + 1)

        return visit(root, 0)
