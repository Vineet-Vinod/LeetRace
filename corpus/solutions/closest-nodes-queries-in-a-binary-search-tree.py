class Solution:
    def closestNodes(
        self, root: Optional[TreeNode], queries: List[int]
    ) -> List[List[int]]:
        values = []

        def inorder(node: Optional[TreeNode]) -> None:
            if node is not None:
                inorder(node.left)
                values.append(node.val)
                inorder(node.right)

        inorder(root)
        answers = []
        for query in queries:
            index = bisect_left(values, query)
            floor = (
                values[index]
                if index < len(values) and values[index] == query
                else (values[index - 1] if index else -1)
            )
            ceiling = values[index] if index < len(values) else -1
            answers.append([floor, ceiling])
        return answers
