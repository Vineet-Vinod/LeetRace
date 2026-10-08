from typing import List


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        from bisect import bisect_left, bisect_right

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        products = [
            nums1[0] * nums2[0],
            nums1[0] * nums2[-1],
            nums1[-1] * nums2[0],
            nums1[-1] * nums2[-1],
        ]
        low, high = min(products), max(products)
        while low < high:
            middle = (low + high) // 2
            count = 0
            for value in nums1:
                if value > 0:
                    count += bisect_right(nums2, middle // value)
                elif value < 0:
                    threshold = -((-middle) // value)
                    count += len(nums2) - bisect_left(nums2, threshold)
                elif middle >= 0:
                    count += len(nums2)
            if count >= k:
                high = middle
            else:
                low = middle + 1
        return low
