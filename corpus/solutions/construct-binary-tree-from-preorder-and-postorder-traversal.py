class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        positions = {value: index for index, value in enumerate(postorder)}

        def build(
            pre_start: int, pre_end: int, post_start: int, post_end: int
        ) -> Optional[TreeNode]:
            if pre_start > pre_end:
                return None
            root = TreeNode(preorder[pre_start])
            if pre_start == pre_end:
                return root
            left_root = preorder[pre_start + 1]
            left_end = positions[left_root]
            left_size = left_end - post_start + 1
            root.left = build(
                pre_start + 1, pre_start + left_size, post_start, left_end
            )
            root.right = build(
                pre_start + left_size + 1, pre_end, left_end + 1, post_end - 1
            )
            return root

        return build(0, len(preorder) - 1, 0, len(postorder) - 1)
