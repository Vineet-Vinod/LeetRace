class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if left is None or right is None:
                if left is not right:
                    return False
            elif left.val != right.val:
                return False
            else:
                stack.extend(((left.left, right.right), (left.right, right.left)))
        return True
