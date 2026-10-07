class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        first = second = None
        count_first = count_second = 0
        for value in nums:
            if first == value:
                count_first += 1
            elif second == value:
                count_second += 1
            elif count_first == 0:
                first, count_first = value, 1
            elif count_second == 0:
                second, count_second = value, 1
            else:
                count_first -= 1
                count_second -= 1
        result = [
            value
            for value in (first, second)
            if value is not None and nums.count(value) > len(nums) // 3
        ]
        return sorted(result)
