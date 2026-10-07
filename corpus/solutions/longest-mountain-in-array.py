class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        longest = 0
        index = 1
        while index < len(arr) - 1:
            if arr[index - 1] < arr[index] > arr[index + 1]:
                left = index - 1
                right = index + 1
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1
                while right + 1 < len(arr) and arr[right] > arr[right + 1]:
                    right += 1
                longest = max(longest, right - left + 1)
                index = right
            else:
                index += 1
        return longest
