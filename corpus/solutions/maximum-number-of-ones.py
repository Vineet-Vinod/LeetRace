class Solution:
    def maximumNumberOfOnes(
        self, width: int, height: int, sideLength: int, maxOnes: int
    ) -> int:
        counts = []
        for row in range(sideLength):
            for col in range(sideLength):
                counts.append(
                    ((height - 1 - row) // sideLength + 1)
                    * ((width - 1 - col) // sideLength + 1)
                )
        return sum(sorted(counts, reverse=True)[:maxOnes])
