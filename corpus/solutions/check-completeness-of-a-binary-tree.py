class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        saw_gap = False
        while queue:
            node = queue.popleft()
            if node is None:
                saw_gap = True
                continue
            if saw_gap:
                return False
            queue.append(node.left)
            queue.append(node.right)
        return True
