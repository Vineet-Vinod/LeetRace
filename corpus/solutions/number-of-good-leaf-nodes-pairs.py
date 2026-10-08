class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        pairs = 0

        def leaf_distances(node: Optional[TreeNode]) -> List[int]:
            nonlocal pairs
            if node is None:
                return []
            if node.left is None and node.right is None:
                return [1]
            left = leaf_distances(node.left)
            right = leaf_distances(node.right)
            for left_distance in left:
                for right_distance in right:
                    if left_distance + right_distance <= distance:
                        pairs += 1
            return [value + 1 for value in left + right if value + 1 < distance]

        leaf_distances(root)
        return pairs
