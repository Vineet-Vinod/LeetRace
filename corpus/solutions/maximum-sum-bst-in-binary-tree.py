class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        stack = [(root, False)]
        info = {None: (True, float("inf"), -float("inf"), 0)}
        answer = 0
        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
            if not visited:
                stack.extend(((node, True), (node.right, False), (node.left, False)))
                continue
            lv, lmin, lmax, lsum = info[node.left]
            rv, rmin, rmax, rsum = info[node.right]
            valid = lv and rv and lmax < node.val < rmin
            total = lsum + rsum + node.val
            info[node] = (valid, min(lmin, node.val), max(rmax, node.val), total)
            if valid:
                answer = max(answer, total)
        return answer
