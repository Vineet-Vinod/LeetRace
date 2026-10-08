from __future__ import annotations
from typing import Optional


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        i = 0
        while i < len(traversal):
            depth = 0
            while traversal[i] == "-":
                depth += 1
                i += 1
            start = i
            while i < len(traversal) and traversal[i].isdigit():
                i += 1
            node = TreeNode(int(traversal[start:i]))
            while len(stack) > depth:
                stack.pop()
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            stack.append(node)
        return stack[0]
