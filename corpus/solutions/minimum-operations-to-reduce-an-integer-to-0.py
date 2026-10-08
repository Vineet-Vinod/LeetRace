class Solution:
    def minOperations(self, n: int) -> int:
        operations = 0
        while n:
            if n & 1:
                if n == 1 or n & 3 == 1:
                    n -= 1
                else:
                    n += 1
                operations += 1
            else:
                n >>= 1
        return operations
