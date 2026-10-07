class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return -1
        queue = deque([root])
        sums = []
        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            sums.append(level_sum)
        if k > len(sums):
            return -1
        sums.sort(reverse=True)
        return sums[k - 1]
