class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ordered = sorted(nums)
        groups: list[list[int]] = []
        for i in range(0, len(ordered), 3):
            group = ordered[i : i + 3]
            if group[-1] - group[0] > k:
                return []
            groups.append(group)
        return groups
