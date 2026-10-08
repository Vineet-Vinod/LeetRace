class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0] * n
        pairs = 0
        answer: list[int] = []
        for index, color in queries:
            if colors[index]:
                pairs -= int(index > 0 and colors[index - 1] == colors[index])
                pairs -= int(index + 1 < n and colors[index + 1] == colors[index])
            colors[index] = color
            pairs += int(index > 0 and colors[index - 1] == color)
            pairs += int(index + 1 < n and colors[index + 1] == color)
            answer.append(pairs)
        return answer
