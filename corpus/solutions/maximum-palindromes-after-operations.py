class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        pairs = sum(count // 2 for count in Counter("".join(words)).values())
        answer = 0
        for length in sorted(map(len, words)):
            needed = length // 2
            if pairs < needed:
                break
            pairs -= needed
            answer += 1
        return answer
