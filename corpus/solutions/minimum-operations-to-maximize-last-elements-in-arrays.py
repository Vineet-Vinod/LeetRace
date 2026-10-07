class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        def count(swapped_last: bool) -> int:
            last1, last2 = nums1[-1], nums2[-1]
            if swapped_last:
                last1, last2 = last2, last1
            operations = int(swapped_last)
            for i in range(len(nums1) - 1):
                first, second = nums1[i], nums2[i]
                if first <= last1 and second <= last2:
                    continue
                if second <= last1 and first <= last2:
                    operations += 1
                else:
                    return len(nums1) + 1
            return operations

        answer = min(count(False), count(True))
        return -1 if answer > len(nums1) else answer
