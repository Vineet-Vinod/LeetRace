class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct = sorted(set(nums), reverse=True)
        return distinct[2] if len(distinct) >= 3 else distinct[0]
