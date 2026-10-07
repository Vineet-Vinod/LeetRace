class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        ordered = sorted(points, key=lambda p: (p[0], -p[1]))
        answer = 0
        for i, (_, top) in enumerate(ordered):
            highest = -(10**30)
            for j in range(i + 1, len(ordered)):
                bottom = ordered[j][1]
                if highest < bottom <= top:
                    answer += 1
                    highest = bottom
        return answer
