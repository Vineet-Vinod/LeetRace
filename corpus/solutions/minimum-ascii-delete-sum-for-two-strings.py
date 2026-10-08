class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        previous = [0]
        for char in s2:
            previous.append(previous[-1] + ord(char))
        for first in s1:
            current = [previous[0] + ord(first)]
            for j, second in enumerate(s2, start=1):
                if first == second:
                    current.append(previous[j - 1])
                else:
                    current.append(
                        min(previous[j] + ord(first), current[j - 1] + ord(second))
                    )
            previous = current
        return previous[-1]
