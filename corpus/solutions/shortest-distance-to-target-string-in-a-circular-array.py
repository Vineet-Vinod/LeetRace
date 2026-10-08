class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        distances = [
            min(abs(index - startIndex), len(words) - abs(index - startIndex))
            for index, word in enumerate(words)
            if word == target
        ]
        return min(distances, default=-1)
