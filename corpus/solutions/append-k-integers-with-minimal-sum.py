class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        present = sorted(set(nums))
        total = 0
        next_value = 1
        remaining = k
        for value in present:
            if value > next_value:
                take = min(remaining, value - next_value)
                total += (next_value + next_value + take - 1) * take // 2
                remaining -= take
                if remaining == 0:
                    return total
            next_value = value + 1
        return total + remaining * (2 * next_value + remaining - 1) // 2
