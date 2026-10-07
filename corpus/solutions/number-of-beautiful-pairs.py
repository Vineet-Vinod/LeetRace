class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        first = [int(str(x)[0]) for x in nums]
        return sum(
            math.gcd(first[i], nums[j] % 10) == 1
            for i in range(len(nums))
            for j in range(i + 1, len(nums))
        )
