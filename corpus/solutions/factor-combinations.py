class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        result: List[List[int]] = []

        def search(remaining: int, minimum: int, path: List[int]) -> None:
            factor = minimum
            while factor * factor <= remaining:
                if remaining % factor == 0:
                    quotient = remaining // factor
                    result.append(path + [factor, quotient])
                    search(quotient, factor, path + [factor])
                factor += 1

        search(n, 2, [])
        return sorted(result)
