class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr).values()
        return len(set(counts)) == len(list(counts))
