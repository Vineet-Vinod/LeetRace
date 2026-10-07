class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        stack = [(root, False)]
        gains = {}
        answer = -(10**30)
        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
            if not visited:
                stack.extend([(node, True), (node.right, False), (node.left, False)])
            else:
                left = max(0, gains.get(node.left, 0))
                right = max(0, gains.get(node.right, 0))
                answer = max(answer, node.val + left + right)
                gains[node] = node.val + max(left, right)
        return answer
