class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        first = sorted(nums1)
        second = sorted(nums2)
        valid = []
        for removed in range(3):
            shift = second[0] - first[removed]
            i = removed
            j = 0
            while i < len(first) and j < len(second):
                if first[i] + shift == second[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            if j == len(second):
                valid.append(shift)
        return min(valid)
