class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        previous = [0] * (len(target) + 1)
        longest = 0
        for left in initial:
            current = [0] * (len(target) + 1)
            for j, right in enumerate(target, 1):
                if left == right:
                    current[j] = previous[j - 1] + 1
                    longest = max(longest, current[j])
            previous = current
        return len(initial) + len(target) - 2 * longest
