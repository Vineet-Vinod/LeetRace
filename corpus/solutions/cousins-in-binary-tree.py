class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque([(root, None, 0)])
        found = {}
        while queue:
            node, parent, depth = queue.popleft()
            if node.val in (x, y):
                found[node.val] = (parent, depth)
            if node.left:
                queue.append((node.left, node, depth + 1))
            if node.right:
                queue.append((node.right, node, depth + 1))
        return found[x][1] == found[y][1] and found[x][0] is not found[y][0]
