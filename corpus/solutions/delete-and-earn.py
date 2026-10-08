class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = Counter(nums)
        two_back = one_back = 0
        previous = 0
        for value in sorted(points):
            best = max(
                one_back,
                two_back + value * points[value]
                if value == previous + 1
                else one_back + value * points[value],
            )
            two_back, one_back, previous = one_back, best, value
        return one_back
