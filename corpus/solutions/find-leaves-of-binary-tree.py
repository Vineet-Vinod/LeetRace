class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> list[list[int]]:
        levels: dict[int, list[int]] = {}
        heights: dict[int, int] = {}
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if not visited:
                stack.append((node, True))
                if node.right is not None:
                    stack.append((node.right, False))
                if node.left is not None:
                    stack.append((node.left, False))
            else:
                height = 1 + max(
                    heights.get(id(node.left), 0), heights.get(id(node.right), 0)
                )
                heights[id(node)] = height
                levels.setdefault(height, []).append(node.val)
        return [levels[level] for level in range(1, max(levels, default=0) + 1)]
