class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        target = root.val
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val != target:
                return False
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return True
