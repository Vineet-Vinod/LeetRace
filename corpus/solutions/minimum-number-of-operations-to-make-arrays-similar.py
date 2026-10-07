class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        first = sorted(nums, key=lambda x: (x % 2, x))
        second = sorted(target, key=lambda x: (x % 2, x))
        return sum(abs(a - b) for a, b in zip(first, second)) // 4
