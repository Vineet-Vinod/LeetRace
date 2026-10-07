class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: list[int], indexDiff: int, valueDiff: int
    ) -> bool:
        buckets = {}
        width = valueDiff + 1
        for i, x in enumerate(nums):
            b = x // width
            if (
                b in buckets
                or (b - 1 in buckets and x - buckets[b - 1] <= valueDiff)
                or (b + 1 in buckets and buckets[b + 1] - x <= valueDiff)
            ):
                return True
            buckets[b] = x
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // width]
        return False
