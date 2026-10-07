class Solution:
    def magicalString(self, n: int) -> int:
        if n == 1:
            return 1
        sequence = [1, 2, 2]
        read = 2
        next_value = 1
        while len(sequence) < n:
            sequence.extend([next_value] * sequence[read])
            read += 1
            next_value = 3 - next_value
        return sequence[:n].count(1)
