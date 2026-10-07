class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color = {}
        color_count = Counter()
        answer = []
        for ball, color in queries:
            previous = ball_color.get(ball)
            if previous is not None:
                color_count[previous] -= 1
                if color_count[previous] == 0:
                    del color_count[previous]
            ball_color[ball] = color
            color_count[color] += 1
            answer.append(len(color_count))
        return answer
