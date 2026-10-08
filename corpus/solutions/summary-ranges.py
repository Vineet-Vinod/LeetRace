class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result: list[str] = []
        index = 0
        while index < len(nums):
            start = nums[index]
            end = start
            index += 1
            while index < len(nums) and nums[index] == end + 1:
                end = nums[index]
                index += 1
            result.append(str(start) if start == end else f"{start}->{end}")
        return result
