class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        positions = {value: index for index, value in enumerate(inorder)}
        preorder_index = 0

        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal preorder_index
            if left >= right:
                return None
            value = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode(value)
            split = positions[value]
            root.left = build(left, split)
            root.right = build(split + 1, right)
            return root

        return build(0, len(inorder))
