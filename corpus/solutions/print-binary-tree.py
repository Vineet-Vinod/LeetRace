class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def height(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            return 1 + max(height(node.left), height(node.right))

        depth = height(root)
        width = (1 << depth) - 1
        result = [[""] * width for _ in range(depth)]

        def place(node: Optional[TreeNode], row: int, left: int, right: int) -> None:
            if node is None:
                return
            middle = (left + right) // 2
            result[row][middle] = str(node.val)
            place(node.left, row + 1, left, middle - 1)
            place(node.right, row + 1, middle + 1, right)

        place(root, 0, 0, width - 1)
        return result
