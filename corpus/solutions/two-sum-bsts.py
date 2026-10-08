class Solution:
    def twoSumBSTs(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int
    ) -> bool:
        values = set()
        stack = [root1]
        while stack:
            node = stack.pop()
            if node is not None:
                values.add(node.val)
                stack.extend((node.left, node.right))
        stack = [root2]
        while stack:
            node = stack.pop()
            if node is not None:
                if target - node.val in values:
                    return True
                stack.extend((node.left, node.right))
        return False
