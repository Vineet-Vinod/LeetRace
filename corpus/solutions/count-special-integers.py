from math import perm


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        digits = list(map(int, str(n)))
        answer = sum(9 * perm(9, length - 1) for length in range(1, len(digits)))
        used = set()
        for i, digit in enumerate(digits):
            for choice in range(1 if i == 0 else 0, digit):
                if choice not in used:
                    answer += perm(9 - i, len(digits) - i - 1)
            if digit in used:
                break
            used.add(digit)
        else:
            answer += 1
        return answer
