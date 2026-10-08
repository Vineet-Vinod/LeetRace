from typing import List


class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        counts = [digits.count(d) for d in range(10)]
        remainder = sum(digits) % 3
        if remainder:
            first = [d for d in range(10) if d % 3 == remainder and counts[d]]
            if first:
                counts[first[0]] -= 1
            else:
                needed = 2
                for d in range(10):
                    if d % 3 == 3 - remainder:
                        taken = min(needed, counts[d])
                        counts[d] -= taken
                        needed -= taken
                if needed:
                    return ""
        result = "".join(str(d) * counts[d] for d in range(9, -1, -1))
        return "0" if result and result[0] == "0" else result
