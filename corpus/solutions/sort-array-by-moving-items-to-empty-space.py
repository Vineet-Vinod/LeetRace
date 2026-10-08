class Solution:
    def sortArray(self, nums: list[int]) -> int:
        n = len(nums)

        def cost(shift: int) -> int:
            seen = [False] * n
            total = 0
            for i in range(n):
                if seen[i]:
                    continue
                j = i
                length = 0
                contains_zero = False
                while not seen[j]:
                    seen[j] = True
                    length += 1
                    contains_zero = contains_zero or nums[j] == 0
                    j = (nums[j] - shift) % n
                if length > 1:
                    total += length - 1 if contains_zero else length + 1
            return total

        return min(cost(0), cost(1))
