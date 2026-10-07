class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_indices = [i for i, value in enumerate(nums) if value == key]
        return [
            i for i in range(len(nums)) if any(abs(i - j) <= k for j in key_indices)
        ]
