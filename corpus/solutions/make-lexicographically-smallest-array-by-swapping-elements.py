class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        ordered = sorted((value, index) for index, value in enumerate(nums))
        result = nums[:]
        start = 0
        while start < len(ordered):
            end = start + 1
            while end < len(ordered) and ordered[end][0] - ordered[end - 1][0] <= limit:
                end += 1
            values = sorted(value for value, _ in ordered[start:end])
            indices = sorted(index for _, index in ordered[start:end])
            for index, value in zip(indices, values):
                result[index] = value
            start = end
        return result
