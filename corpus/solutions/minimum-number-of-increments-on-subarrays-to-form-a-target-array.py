class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        return target[0] + sum(max(0, b - a) for a, b in zip(target, target[1:]))
