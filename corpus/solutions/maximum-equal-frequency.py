class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        frequencies = defaultdict(int)
        highest = answer = 0
        for size, value in enumerate(nums, 1):
            old = counts[value]
            frequencies[old] -= 1
            counts[value] += 1
            frequencies[old + 1] += 1
            highest = max(highest, old + 1)
            if (
                highest == 1
                or highest * frequencies[highest] + 1 == size
                or (highest - 1) * (frequencies[highest - 1] + 1) + 1 == size
                and frequencies[highest] == 1
            ):
                answer = size
        return answer
