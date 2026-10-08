class Solution:
    def uniqueLetterString(self, s: str) -> int:
        previous: dict[str, tuple[int, int]] = {}
        answer = 0
        for i, char in enumerate(s):
            before, last = previous.get(char, (-1, -1))
            answer += (last - before) * (i - last)
            previous[char] = (last, i)
        for before, last in previous.values():
            answer += (last - before) * (len(s) - last)
        return answer
