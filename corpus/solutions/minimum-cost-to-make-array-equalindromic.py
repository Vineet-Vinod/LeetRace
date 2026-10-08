def make_palindrome(prefix: int, length: int) -> int:
    first = str(prefix)
    half_length = (length + 1) // 2
    if len(first) != half_length:
        return -1
    suffix = first[:-1] if length % 2 else first
    return int(first + suffix[::-1])


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ordered = sorted(nums)
        middle = ordered[len(ordered) // 2]
        text = str(middle)
        half_length = (len(text) + 1) // 2
        prefix = int(text[:half_length])
        candidates = {1, 9, 11, 101, 999999999}
        for candidate_prefix in (prefix - 1, prefix, prefix + 1):
            value = make_palindrome(candidate_prefix, len(text))
            if 1 <= value < 10**9:
                candidates.add(value)
        if len(text) < 9:
            candidates.add(10 ** len(text) + 1)
        if len(text) > 1:
            candidates.add(10 ** (len(text) - 1) - 1)
        return min(
            sum(abs(value - candidate) for value in nums)
            for candidate in candidates
            if candidate > 0
        )
