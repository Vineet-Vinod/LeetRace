class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        matches = 0
        width = len(pattern)
        for start in range(len(nums) - width):
            valid = True
            for offset, relation in enumerate(pattern):
                left, right = nums[start + offset], nums[start + offset + 1]
                if (
                    relation == 1
                    and left >= right
                    or relation == 0
                    and left != right
                    or relation == -1
                    and left <= right
                ):
                    valid = False
                    break
            matches += valid
        return matches
