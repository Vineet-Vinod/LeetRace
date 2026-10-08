class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        def path(node: Optional[TreeNode], target: int) -> List[int]:
            if node is None:
                return []
            if node.val == target:
                return [node.val]
            child_path = path(node.left, target) or path(node.right, target)
            return [node.val] + child_path if child_path else []

        first = path(root, p)
        second = path(root, q)
        common = 0
        while common < min(len(first), len(second)) and first[common] == second[common]:
            common += 1
        return len(first) + len(second) - 2 * common
