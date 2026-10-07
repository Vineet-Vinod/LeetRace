class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def count(squares: List[int], values: List[int]) -> int:
            frequencies = Counter(values)
            result = 0
            for value in squares:
                target = value * value
                for left, amount in frequencies.items():
                    if target % left == 0:
                        right = target // left
                        if left <= right and right in frequencies:
                            result += (
                                amount * (amount - 1) // 2
                                if left == right
                                else amount * frequencies[right]
                            )
            return result

        return count(nums1, nums2) + count(nums2, nums1)
