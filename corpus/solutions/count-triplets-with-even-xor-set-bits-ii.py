class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        parity_counts = []
        for values in (a, b, c):
            even = sum(value.bit_count() % 2 == 0 for value in values)
            parity_counts.append((even, len(values) - even))
        answer = 0
        for first in (0, 1):
            for second in (0, 1):
                third = first ^ second
                answer += (
                    parity_counts[0][first]
                    * parity_counts[1][second]
                    * parity_counts[2][third]
                )
        return answer
