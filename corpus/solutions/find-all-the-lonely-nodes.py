class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            if node.left and not node.right:
                result.append(node.left.val)
            if node.right and not node.left:
                result.append(node.right.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return sorted(result)
