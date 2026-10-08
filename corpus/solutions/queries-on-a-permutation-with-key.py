class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        permutation = list(range(1, m + 1))
        result = []
        for value in queries:
            index = permutation.index(value)
            result.append(index)
            permutation.pop(index)
            permutation.insert(0, value)
        return result
