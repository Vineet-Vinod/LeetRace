class Solution:
    def isValidBST(self, root) -> bool:
        stack = [(root, float("-inf"), float("inf"))]
        while stack:
            node, low, high = stack.pop()
            if not node:
                continue
            if not low < node.val < high:
                return False
            stack.append((node.right, node.val, high))
            stack.append((node.left, low, node.val))
        return True
