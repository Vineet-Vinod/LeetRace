class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        distinct = set()
        for start in range(len(nums)):
            divisible = 0
            current = []
            for end in range(start, len(nums)):
                divisible += nums[end] % p == 0
                if divisible > k:
                    break
                current.append(nums[end])
                distinct.add(tuple(current))
        return len(distinct)
