from typing import Optional
from heapq import merge


class Solution:
    def countGreatEnoughNodes(self, root: Optional[TreeNode], k: int) -> int:
        stack = [(root, False)]
        smallest = {}
        answer = 0
        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
            if not visited:
                stack.extend([(node, True), (node.right, False), (node.left, False)])
            else:
                values = list(
                    merge(smallest.pop(node.left, []), smallest.pop(node.right, []))
                )[:k]
                if len(values) == k and values[-1] < node.val:
                    answer += 1
                smallest[node] = sorted(values + [node.val])[:k]
        return answer
