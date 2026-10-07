class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            a, b = stack.pop()
            if a is None or b is None:
                if a is not b:
                    return False
            elif a.val != b.val:
                return False
            else:
                stack.extend(((a.left, b.left), (a.right, b.right)))
        return True
