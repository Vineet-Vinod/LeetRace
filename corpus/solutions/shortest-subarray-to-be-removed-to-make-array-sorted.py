class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        size = len(arr)
        left = 0
        while left + 1 < size and arr[left] <= arr[left + 1]:
            left += 1
        if left == size - 1:
            return 0
        right = size - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        answer = min(size - left - 1, right)
        i = 0
        j = right
        while i <= left and j < size:
            if arr[i] <= arr[j]:
                answer = min(answer, j - i - 1)
                i += 1
            else:
                j += 1
        return answer
