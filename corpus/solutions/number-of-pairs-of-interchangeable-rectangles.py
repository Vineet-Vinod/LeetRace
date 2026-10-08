class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratios = Counter(
            (width // math.gcd(width, height), height // math.gcd(width, height))
            for width, height in rectangles
        )
        return sum(count * (count - 1) // 2 for count in ratios.values())
