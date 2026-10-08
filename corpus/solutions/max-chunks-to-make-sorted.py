class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        maximum = chunks = 0
        for i, value in enumerate(arr):
            maximum = max(maximum, value)
            if maximum == i:
                chunks += 1
        return chunks
