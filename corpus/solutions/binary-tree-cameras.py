from __future__ import annotations


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        states = {None: 1}
        stack = [(root, False)]
        cameras = 0
        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
            if not visited:
                stack.extend([(node, True), (node.right, False), (node.left, False)])
                continue
            left, right = states[node.left], states[node.right]
            if left == 0 or right == 0:
                cameras += 1
                states[node] = 2
            else:
                states[node] = 1 if left == 2 or right == 2 else 0
        return cameras + (states[root] == 0)
