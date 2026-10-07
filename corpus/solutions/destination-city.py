class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        origins = {start for start, _ in paths}
        return min(end for _, end in paths if end not in origins)
