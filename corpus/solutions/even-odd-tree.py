class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        level = 0
        while queue:
            previous = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if level % 2 == 0:
                    if (
                        node.val % 2 == 0
                        or previous is not None
                        and node.val <= previous
                    ):
                        return False
                elif node.val % 2 == 1 or previous is not None and node.val >= previous:
                    return False
                previous = node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            level += 1
        return True
