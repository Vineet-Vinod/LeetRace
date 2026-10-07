class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counts = [0, 0, 0]
        left = 0
        answer = 0
        for right, char in enumerate(s):
            counts[ord(char) - 97] += 1
            while all(counts):
                answer += len(s) - right
                counts[ord(s[left]) - 97] -= 1
                left += 1
        return answer
