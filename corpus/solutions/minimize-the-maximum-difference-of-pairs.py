class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        nums.sort()
        left, right = 0, nums[-1] - nums[0]

        def can_make(limit: int) -> bool:
            pairs = index = 0
            while index < len(nums) - 1:
                if nums[index + 1] - nums[index] <= limit:
                    pairs += 1
                    index += 2
                else:
                    index += 1
            return pairs >= p

        while left < right:
            middle = (left + right) // 2
            if can_make(middle):
                right = middle
            else:
                left = middle + 1
        return left
