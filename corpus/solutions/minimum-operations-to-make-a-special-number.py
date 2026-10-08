class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)
        best = n
        for first, second in (("0", "0"), ("2", "5"), ("5", "0"), ("7", "5")):
            second_index = num.rfind(second)
            while second_index >= 0:
                first_index = num.rfind(first, 0, second_index)
                if first_index >= 0:
                    best = min(best, n - first_index - 2)
                    break
                second_index = num.rfind(second, 0, second_index)
        if "0" in num:
            best = min(best, n - 1)
        return best
