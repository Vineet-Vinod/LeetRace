class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        result = []
        level = [root]
        while level:
            result.append(sum(node.val for node in level) / len(level))
            next_level = []
            for node in level:
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            level = next_level
        return result
