class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda pair: pair[1])
        count = 0
        end = -float("inf")
        for start, next_end in pairs:
            if start > end:
                count += 1
                end = next_end
        return count
