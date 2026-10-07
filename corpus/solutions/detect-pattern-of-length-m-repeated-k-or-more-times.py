class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        run = 0
        for i in range(len(arr) - m):
            if arr[i] == arr[i + m]:
                run += 1
            else:
                run = 0
            if run >= m * (k - 1):
                return True
        return False
