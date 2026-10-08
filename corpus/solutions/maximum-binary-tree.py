class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack: list[TreeNode] = []
        for value in nums:
            node = TreeNode(value)
            while stack and stack[-1].val < value:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0] if stack else None
