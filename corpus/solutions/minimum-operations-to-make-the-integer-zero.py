class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for operations in range(1, 61):
            remainder = num1 - operations * num2
            if remainder >= operations and remainder.bit_count() <= operations:
                return operations
        return -1
