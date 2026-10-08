class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ordered = sorted(citations, reverse=True)
        h = 0
        for count, citation in enumerate(ordered, start=1):
            if citation < count:
                break
            h = count
        return h
