class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen: set[int] = set()
        stack = [root] if root is not None else []
        while stack:
            node = stack.pop()
            if k - node.val in seen:
                return True
            seen.add(node.val)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return False
