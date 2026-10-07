class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        positions = [0] * n
        for i, value in enumerate(nums2):
            positions[value] = i
        bit = [0] * (n + 1)
        answer = 0
        for seen, value in enumerate(nums1):
            position = positions[value]
            index = position
            left = 0
            while index:
                left += bit[index]
                index -= index & -index
            right = n - 1 - position - (seen - left)
            answer += left * right
            index = position + 1
            while index <= n:
                bit[index] += 1
                index += index & -index
        return answer
