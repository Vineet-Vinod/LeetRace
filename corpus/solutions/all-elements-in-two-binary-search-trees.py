class Solution:
    def getAllElements(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> List[int]:
        values: List[int] = []
        for root in (root1, root2):
            stack: List[TreeNode] = []
            node = root
            while node is not None or stack:
                while node is not None:
                    stack.append(node)
                    node = node.left
                node = stack.pop()
                values.append(node.val)
                node = node.right
        values.sort()
        return values
