class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out: List[int] = []
        stack = [] if root is None else [root]
        while stack:
            node = stack.pop()
            out.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return out
