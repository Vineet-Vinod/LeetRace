class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        index = 0

        def build(lower: int, upper: int) -> Optional[TreeNode]:
            nonlocal index
            if index == len(preorder) or not lower < preorder[index] < upper:
                return None
            value = preorder[index]
            index += 1
            node = TreeNode(value)
            node.left = build(lower, value)
            node.right = build(value, upper)
            return node

        return build(float("-inf"), float("inf"))
