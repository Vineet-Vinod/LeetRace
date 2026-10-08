class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        boundary = [root.val]
        node = root.left
        while node is not None:
            if node.left is not None or node.right is not None:
                boundary.append(node.val)
            node = node.left if node.left is not None else node.right

        def add_leaves(current: Optional[TreeNode]) -> None:
            if current is None:
                return
            if current.left is None and current.right is None:
                boundary.append(current.val)
                return
            add_leaves(current.left)
            add_leaves(current.right)

        add_leaves(root.left)
        add_leaves(root.right)
        right_boundary = []
        node = root.right
        while node is not None:
            if node.left is not None or node.right is not None:
                right_boundary.append(node.val)
            node = node.right if node.right is not None else node.left
        boundary.extend(reversed(right_boundary))
        return boundary
