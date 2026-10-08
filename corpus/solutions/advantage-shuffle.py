class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        available = sorted(nums1)
        order = sorted(range(len(nums2)), key=lambda i: (-nums2[i], i))
        result = [0] * len(nums2)
        low = 0
        high = len(available) - 1
        for index in order:
            if available[high] > nums2[index]:
                result[index] = available[high]
                high -= 1
            else:
                result[index] = available[low]
                low += 1
        return result
