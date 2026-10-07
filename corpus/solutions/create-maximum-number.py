class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        def pick(nums: list[int], size: int) -> list[int]:
            drops = len(nums) - size
            stack = []
            for value in nums:
                while drops and stack and stack[-1] < value:
                    stack.pop()
                    drops -= 1
                stack.append(value)
            return stack[:size]

        best = []
        for size in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            a, b = pick(nums1, size), pick(nums2, k - size)
            merged = []
            i = j = 0
            while i < len(a) or j < len(b):
                if a[i:] > b[j:]:
                    merged.append(a[i])
                    i += 1
                else:
                    merged.append(b[j])
                    j += 1
            best = max(best, merged)
        return best
