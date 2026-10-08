class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        flips: list[int] = []
        position = 0

        def visit(node: Optional[TreeNode]) -> bool:
            nonlocal position
            if node is None:
                return True
            if position >= len(voyage) or voyage[position] != node.val:
                return False
            position += 1
            if (
                node.left is not None
                and position < len(voyage)
                and node.left.val != voyage[position]
            ):
                flips.append(node.val)
                return visit(node.right) and visit(node.left)
            return visit(node.left) and visit(node.right)

        if not visit(root) or position != len(voyage):
            return [-1]
        return sorted(flips)
