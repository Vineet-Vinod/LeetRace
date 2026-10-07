class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        count_a = [0] * 26
        count_b = [0] * 26
        for ch in a:
            count_a[ord(ch) - 97] += 1
        for ch in b:
            count_b[ord(ch) - 97] += 1
        answer = min(len(a), len(b))
        for letter in range(25):
            answer = min(
                answer, sum(count_a[letter + 1 :]) + sum(count_b[: letter + 1])
            )
            answer = min(
                answer, sum(count_b[letter + 1 :]) + sum(count_a[: letter + 1])
            )
        for letter in range(26):
            answer = min(answer, len(a) + len(b) - count_a[letter] - count_b[letter])
        return answer
