class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        modulo = 10**9 + 7
        stack = []
        total = 0
        for index in range(len(arr) + 1):
            while stack and (index == len(arr) or arr[stack[-1]] >= arr[index]):
                middle = stack.pop()
                previous = stack[-1] if stack else -1
                total += arr[middle] * (middle - previous) * (index - middle)
            stack.append(index)
        return total % modulo
