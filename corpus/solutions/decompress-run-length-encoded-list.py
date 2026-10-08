class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        out: List[int] = []
        for i in range(0, len(nums), 2):
            out.extend([nums[i + 1]] * nums[i])
        return out
