class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3:
            return False
        target = total // 3
        parts = 0
        running = 0
        for index, value in enumerate(arr):
            running += value
            if running == target:
                parts += 1
                running = 0
                if parts == 2 and index < len(arr) - 1:
                    return True
        return False
