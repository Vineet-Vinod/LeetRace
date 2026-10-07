class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        left, right = 0, len(tokens) - 1
        score = best = 0
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                left += 1
                score += 1
                best = max(best, score)
            elif score and left < right:
                power += tokens[right]
                right -= 1
                score -= 1
            else:
                break
        return best
