class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        a = b = -1
        answer = 0
        for start, end in sorted(
            intervals, key=lambda interval: (interval[1], -interval[0])
        ):
            if start > b:
                a, b = end - 1, end
                answer += 2
            elif start > a:
                a, b = b, end
                answer += 1
        return answer
