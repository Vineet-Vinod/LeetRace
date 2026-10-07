class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.val = 0
        queue = deque([root])
        while queue:
            level = list(queue)
            child_total = sum(
                child.val
                for node in level
                for child in (node.left, node.right)
                if child is not None
            )
            for node in level:
                sibling_total = (node.left.val if node.left else 0) + (
                    node.right.val if node.right else 0
                )
                for child in (node.left, node.right):
                    if child is not None:
                        child.val = child_total - sibling_total
                        queue.append(child)
                queue.popleft()
        return root
