class Solution:
    def minFlips(self, s: str) -> int:
        size = len(s)
        doubled = s + s
        mismatch_zero = 0
        mismatch_one = 0
        best = size
        for index, char in enumerate(doubled):
            expected = "0" if index % 2 == 0 else "1"
            mismatch_zero += char != expected
            mismatch_one += char == expected
            if index >= size:
                outgoing_expected = "0" if (index - size) % 2 == 0 else "1"
                mismatch_zero -= doubled[index - size] != outgoing_expected
                mismatch_one -= doubled[index - size] == outgoing_expected
            if index >= size - 1:
                best = min(best, mismatch_zero, mismatch_one)
        return best
