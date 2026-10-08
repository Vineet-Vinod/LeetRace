class Solution:
    def numberOfNodes(self, n: int, queries: List[int]) -> int:
        changes = [0] * (n + 2)
        for node in queries:
            left = node
            width = 1
            while left <= n:
                right = min(n, left + width - 1)
                changes[left] += 1
                changes[right + 1] -= 1
                left *= 2
                width *= 2
        parity = 0
        ones = 0
        for label in range(1, n + 1):
            parity += changes[label]
            ones += parity % 2
        return ones
