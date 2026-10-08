class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        signature = sorted(str(n))
        value = 1
        while value <= 10**9:
            if sorted(str(value)) == signature:
                return True
            value *= 2
        return False
