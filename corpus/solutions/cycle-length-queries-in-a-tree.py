class Solution:
    def cycleLengthQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        out = []
        for a, b in queries:
            length = 1
            while a != b:
                if a > b:
                    a //= 2
                else:
                    b //= 2
                length += 1
            out.append(length)
        return out
