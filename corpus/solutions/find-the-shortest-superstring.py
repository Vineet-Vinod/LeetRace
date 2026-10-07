class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        extra = [[words[j] for j in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    for size in range(min(len(words[i]), len(words[j])), 0, -1):
                        if words[i].endswith(words[j][:size]):
                            extra[i][j] = words[j][size:]
                            break
        dp = [{} for _ in range(1 << n)]
        for i, word in enumerate(words):
            dp[1 << i][i] = word
        for mask in range(1, 1 << n):
            for last, text in dp[mask].items():
                for nxt in range(n):
                    if mask >> nxt & 1:
                        continue
                    new_mask = mask | (1 << nxt)
                    candidate = text + extra[last][nxt]
                    previous = dp[new_mask].get(nxt)
                    if previous is None or (len(candidate), candidate) < (
                        len(previous),
                        previous,
                    ):
                        dp[new_mask][nxt] = candidate
        return min(dp[-1].values(), key=lambda text: (len(text), text))
