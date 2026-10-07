class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = Counter(arr)
        distinct = [value for value in arr if counts[value] == 1]
        return distinct[k - 1] if k <= len(distinct) else ""
