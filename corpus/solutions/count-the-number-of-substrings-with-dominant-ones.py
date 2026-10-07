class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        zeros = [index for index, char in enumerate(s) if char == "0"]
        total = 0
        zero_count = len(zeros)
        limit = math.isqrt(len(s)) + 1
        for start in range(len(s)):
            first = bisect_left(zeros, start)
            next_zero = zeros[first] if first < zero_count else len(s)
            total += next_zero - start
            for count in range(1, limit + 1):
                zero_index = first + count - 1
                if zero_index >= zero_count:
                    break
                leftmost_end = max(zeros[zero_index], start + count * count + count - 1)
                rightmost_end = (
                    zeros[zero_index + 1] - 1
                    if zero_index + 1 < zero_count
                    else len(s) - 1
                )
                if leftmost_end <= rightmost_end:
                    total += rightmost_end - leftmost_end + 1
        return total
