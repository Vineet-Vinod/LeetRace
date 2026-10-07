class Solution:
    def countRectangles(
        self, rectangles: List[List[int]], points: List[List[int]]
    ) -> List[int]:
        by_height: dict[int, list[int]] = defaultdict(list)
        for width, height in rectangles:
            by_height[height].append(width)
        for widths in by_height.values():
            widths.sort()
        answer: list[int] = []
        for x, y in points:
            count = 0
            for height, widths in by_height.items():
                if height >= y:
                    count += len(widths) - bisect_left(widths, x)
            answer.append(count)
        return answer
