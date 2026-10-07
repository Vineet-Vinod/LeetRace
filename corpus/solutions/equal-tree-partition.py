class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        subtree_sums: list[int] = []

        def total(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            value = node.val + total(node.left) + total(node.right)
            subtree_sums.append(value)
            return value

        tree_sum = total(root)
        if tree_sum % 2:
            return False
        target = tree_sum // 2
        return any(value == target for value in subtree_sums[:-1])
