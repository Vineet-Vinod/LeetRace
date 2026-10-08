class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        text = str(n)
        base = len(digits)
        answer = sum(base**length for length in range(1, len(text)))
        for i, char in enumerate(text):
            answer += sum(d < char for d in digits) * base ** (len(text) - i - 1)
            if char not in digits:
                return answer
        return answer + 1
