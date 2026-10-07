class Solution:
    def reinitializePermutation(self, n: int) -> int:
        position = 1
        operations = 0
        while True:
            if position < n // 2:
                position *= 2
            else:
                position = 2 * (position - n // 2) + 1
            operations += 1
            if position == 1:
                return operations
