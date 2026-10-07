class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        return any(
            arr[index] % 2 and arr[index + 1] % 2 and arr[index + 2] % 2
            for index in range(len(arr) - 2)
        )
