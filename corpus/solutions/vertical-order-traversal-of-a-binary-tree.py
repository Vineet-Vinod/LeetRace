from typing import List, Optional


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = []
        stack = [(root, 0, 0)]
        while stack:
            node, row, col = stack.pop()
            if node is None:
                continue
            nodes.append((col, row, node.val))
            stack.append((node.left, row + 1, col - 1))
            stack.append((node.right, row + 1, col + 1))
        answer = []
        last = None
        for col, row, val in sorted(nodes):
            if col != last:
                answer.append([])
                last = col
            answer[-1].append(val)
        return answer
