class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        first = root.val
        second = None
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val > first and (second is None or node.val < second):
                second = node.val
            if node.left is not None:
                stack.append(node.left)
                stack.append(node.right)
        return -1 if second is None else second
