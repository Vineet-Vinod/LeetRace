class Solution:
    def singleDivisorTriplet(self, nums: List[int]) -> int:
        counts = Counter(nums)
        values = sorted(counts)
        total = 0
        for i, first in enumerate(values):
            for j in range(i, len(values)):
                second = values[j]
                for k in range(j, len(values)):
                    third = values[k]
                    divisors = sum(
                        (first + second + third) % value == 0
                        for value in (first, second, third)
                    )
                    if divisors != 1:
                        continue
                    if first == third:
                        ways = counts[first] * (counts[first] - 1) * (counts[first] - 2)
                    elif first == second:
                        ways = counts[first] * (counts[first] - 1) * counts[third] * 3
                    elif second == third:
                        ways = counts[first] * counts[second] * (counts[second] - 1) * 3
                    else:
                        ways = counts[first] * counts[second] * counts[third] * 6
                    total += ways
        return total
