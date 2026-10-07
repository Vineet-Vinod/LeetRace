class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(left == right for left, right in zip(secret, guess))
        secret_counts = Counter(
            left for left, right in zip(secret, guess) if left != right
        )
        guess_counts = Counter(
            right for left, right in zip(secret, guess) if left != right
        )
        cows = sum((secret_counts & guess_counts).values())
        return f"{bulls}A{cows}B"
