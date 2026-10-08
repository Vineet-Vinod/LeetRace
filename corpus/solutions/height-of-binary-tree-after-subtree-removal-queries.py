from __future__ import annotations
from typing import List, Optional


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        order = []
        start, end = {}, {}
        stack = [(root, 0, False)]
        while stack:
            node, depth, done = stack.pop()
            if done:
                end[node.val] = len(order)
                continue
            start[node.val] = len(order)
            order.append(depth)
            stack.append((node, depth, True))
            if node.right:
                stack.append((node.right, depth + 1, False))
            if node.left:
                stack.append((node.left, depth + 1, False))
        prefix = [-1]
        for d in order:
            prefix.append(max(prefix[-1], d))
        suffix = [-1] * (len(order) + 1)
        for i in range(len(order) - 1, -1, -1):
            suffix[i] = max(suffix[i + 1], order[i])
        return [max(prefix[start[q]], suffix[end[q]]) for q in queries]
