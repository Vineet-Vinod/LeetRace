from typing import List


class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        from functools import lru_cache

        numbers = [int(char) for char in s[::2]]
        operators = s[1::2]
        correct = 0
        for term in s.split("+"):
            product = 1
            for number in term.split("*"):
                product *= int(number)
            correct += product

        @lru_cache(None)
        def possible(left: int, right: int) -> frozenset[int]:
            if right - left == 1:
                return frozenset([numbers[left]])
            result: set[int] = set()
            for split in range(left + 1, right):
                for a in possible(left, split):
                    for b in possible(split, right):
                        value = a + b if operators[split - 1] == "+" else a * b
                        # All larger values are equivalent until multiplication by zero.
                        result.add(min(value, 1001))
            return frozenset(result)

        wrong = possible(0, len(numbers))
        return sum(
            5 if value == correct else 2 if value in wrong else 0 for value in answers
        )
