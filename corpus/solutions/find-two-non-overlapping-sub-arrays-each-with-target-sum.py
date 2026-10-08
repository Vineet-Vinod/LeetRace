class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        size = len(arr)
        best_left = [size + 1] * size
        prefix_best = size + 1
        current = left = 0
        answer = size + 1
        for right, value in enumerate(arr):
            current += value
            while current > target:
                current -= arr[left]
                left += 1
            if current == target:
                length = right - left + 1
                if left > 0 and best_left[left - 1] <= size:
                    answer = min(answer, length + best_left[left - 1])
                prefix_best = min(prefix_best, length)
            best_left[right] = prefix_best
        return answer if answer <= size else -1
